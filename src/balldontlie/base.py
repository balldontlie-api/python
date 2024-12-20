import os
from typing import Optional, Dict, Any, List, TypeVar, Generic
import requests
from pydantic import BaseModel, ConfigDict
from .exceptions import (
    BallDontLieException,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError,
)

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    data: T


class ListResponse(BaseResponse[List[T]]):
    pass


class PaginationMeta(BaseModel):
    per_page: Optional[int] = None
    next_cursor: Optional[int] = None


class PaginatedListResponse(BaseResponse[List[T]]):
    meta: PaginationMeta


class BaseAPI(Generic[T]):
    model_class = None

    def __init__(self, client):
        self.client = client

    def _prepare_params(self, params: Dict[str, Any]) -> Dict[str, list[str]]:
        processed = {}
        for key, value in params.items():
            if value is None:
                continue
            if isinstance(value, list):
                processed[f"{key}[]"] = [str(item) for item in value]
            else:
                processed[key] = [str(value)]
        return processed

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = self.client._build_url(path)
        headers = self.client._get_headers()

        try:
            session = requests.Session()

            if params:
                prepared_params = []
                for key, values in params.items():
                    if isinstance(values, list):
                        for value in values:
                            prepared_params.append((key, value))
                    else:
                        prepared_params.append((key, values[0]))
            else:
                prepared_params = None

            response = session.request(
                method=method,
                url=url,
                headers=headers,
                params=prepared_params,
                data=data,
                json=json,
            )

            if not response.ok:
                try:
                    response_data = response.json() if response.content else {}
                except requests.exceptions.JSONDecodeError:
                    response_data = {}

                error_message = response_data.get("error", response.reason)

                if response.status_code == 401:
                    raise AuthenticationError(
                        error_message, response.status_code, response_data
                    )
                elif response.status_code == 429:
                    raise RateLimitError(
                        error_message, response.status_code, response_data
                    )
                elif response.status_code == 400:
                    raise ValidationError(
                        error_message, response.status_code, response_data
                    )
                elif response.status_code == 404:
                    raise NotFoundError(
                        error_message, response.status_code, response_data
                    )
                elif response.status_code >= 500:
                    raise ServerError(
                        error_message, response.status_code, response_data
                    )
                else:
                    raise BallDontLieException(
                        error_message, response.status_code, response_data
                    )

            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                raise BallDontLieException("Invalid JSON response from server")

        except requests.exceptions.RequestException as e:
            raise BallDontLieException(f"Request failed: {str(e)}")
        finally:
            session.close()

    def _get(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return self._request("GET", path, params=params)

    def _get_data(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> BaseResponse[T]:
        processed_params = self._prepare_params(params) if params else None
        response = self._get(path, params=processed_params)

        data = self.model_class(**response["data"])

        return BaseResponse[T](data=data)

    def _get_list(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> ListResponse[T]:
        processed_params = self._prepare_params(params) if params else None
        response = self._get(path, params=processed_params)

        data = [self.model_class(**item) for item in response["data"]]

        return ListResponse[T](data=data)

    def _get_paginated_list(
        self, path: str, params: Dict[str, Any]
    ) -> PaginatedListResponse[T]:
        processed_params = self._prepare_params(params)
        response = self._get(path, params=processed_params)

        print(response)
        data = [self.model_class(**item) for item in response["data"]]

        return PaginatedListResponse[T](data=data, meta=response.get("meta", {}))
