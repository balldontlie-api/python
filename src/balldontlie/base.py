from typing import Optional, Dict, Any, List, TypeVar, Generic
import requests
from pydantic import BaseModel
from .exceptions import BallDontLieException, AuthenticationError, RateLimitError, ValidationError, NotFoundError, ServerError

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    data: T

class ListResponse(BaseResponse[List[T]]):
    pass

class PaginationMeta(BaseModel):
    per_page: Optional[int]
    next_cursor: Optional[int]

class PaginatedListResponse(BaseResponse[List[T]]):
    meta: PaginationMeta

class BaseAPI(Generic[T]):
    model_class = None

    def __init__(self, client):
        self.client = client

    def _prepare_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        processed = {}
        for key, value in params.items():
            if value is None:
                continue
            if isinstance(value, list):
                processed[f"{key}[]"] = value
            else:
                processed[key] = value
        return processed

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        url = f"{self.client.base_url}/{path.lstrip('/')}"
        headers = self.client._get_headers()
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json
            )
            
            if not response.ok:
                response_data = response.json() if response.content else {}
                error_message = response_data.get('error', response.reason)
                
                if response.status_code == 401:
                    raise AuthenticationError(error_message, response.status_code, response_data)
                elif response.status_code == 429:
                    raise RateLimitError(error_message, response.status_code, response_data)
                elif response.status_code == 400:
                    raise ValidationError(error_message, response.status_code, response_data)
                elif response.status_code == 404:
                    raise NotFoundError(error_message, response.status_code, response_data)
                elif response.status_code >= 500:
                    raise ServerError(error_message, response.status_code, response_data)
                else:
                    raise BallDontLieException(error_message, response.status_code, response_data)
            
            return response.json()
                
        except requests.exceptions.RequestException as e:
            raise BallDontLieException(f"Request failed: {str(e)}")

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._request("GET", path, params=params)

    def _get_data(self, path: str, params: Optional[Dict[str, Any]] = None) -> BaseResponse[T]:
        processed_params = self._prepare_params(params) if params else None
        response = self._get(path, params=processed_params)
        data = self.model_class(**response["data"])
        return BaseResponse[T](data=data)

    def _get_list(self, path: str, params: Optional[Dict[str, Any]] = None) -> ListResponse[T]:
        processed_params = self._prepare_params(params) if params else None
        response = self._get(path, params=processed_params)
        data = [self.model_class(**item) for item in response["data"]]
        return ListResponse[T](data=data)

    def _get_paginated_list(self, path: str, params: Dict[str, Any]) -> PaginatedListResponse[T]:
        processed_params = self._prepare_params(params)
        response = self._get(path, params=processed_params)
        data = [self.model_class(**item) for item in response["data"]]
        return PaginatedListResponse[T](
            data=data,
            meta=response.get("meta", {})
        )