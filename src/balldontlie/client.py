from .epl.api import EPLApi
from .nba.api import NBAApi
from .nfl.api import NFLApi
from .mlb.api import MLBApi


class BalldontlieAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.balldontlie.io"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

        self.nba = NBAApi(self)
        self.nfl = NFLApi(self)
        self.mlb = MLBApi(self)
        self.epl = EPLApi(self)

    def _get_headers(self) -> dict:
        return {
            "Authorization": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-bdl-client": "python",
        }

    def _build_url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"
