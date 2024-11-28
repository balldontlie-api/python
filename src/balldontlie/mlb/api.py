from typing import Optional, List
from ..base import BaseAPI, BaseResponse, ListResponse, PaginatedListResponse
from .models import *

class MLBTeamsAPI(BaseAPI[MLBTeam]):
    model_class = MLBTeam

    def list(self, division: Optional[str] = None, league: Optional[str] = None) -> ListResponse[MLBTeam]:
        return self._get_list("mlb/v1/teams", {"division": division, "league": league})

    def get(self, team_id: int) -> BaseResponse[MLBTeam]:
        return self._get_data(f"mlb/v1/teams/{team_id}")

class MLBPlayersAPI(BaseAPI[MLBPlayer]):
    model_class = MLBPlayer

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ) -> PaginatedListResponse[MLBPlayer]:
        return self._get_paginated_list("mlb/v1/players", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids,
            "search": search,
            "first_name": first_name,
            "last_name": last_name
        })

    def get(self, player_id: int) -> BaseResponse[MLBPlayer]:
        return self._get_data(f"mlb/v1/players/{player_id}")

    def list_active(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ) -> PaginatedListResponse[MLBPlayer]:
        return self._get_paginated_list("mlb/v1/players/active", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids,
            "search": search,
            "first_name": first_name,
            "last_name": last_name
        })

class MLBGamesAPI(BaseAPI[MLBGame]):
    model_class = MLBGame

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        dates: Optional[List[str]] = None,
        team_ids: Optional[List[int]] = None,
        seasons: Optional[List[int]] = None,
        postseason: Optional[bool] = None
    ) -> PaginatedListResponse[MLBGame]:
        return self._get_paginated_list("mlb/v1/games", {
            "cursor": cursor,
            "per_page": per_page,
            "dates": dates,
            "team_ids": team_ids,
            "seasons": seasons,
            "postseason": postseason
        })

    def get(self, game_id: int) -> BaseResponse[MLBGame]:
        return self._get_data(f"mlb/v1/games/{game_id}")

class MLBStatsAPI(BaseAPI[MLBStats]):
    model_class = MLBStats

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        player_ids: Optional[List[int]] = None,
        game_ids: Optional[List[int]] = None,
        seasons: Optional[List[int]] = None
    ) -> PaginatedListResponse[MLBStats]:
        return self._get_paginated_list("mlb/v1/stats", {
            "cursor": cursor,
            "per_page": per_page,
            "player_ids": player_ids,
            "game_ids": game_ids,
            "seasons": seasons
        })

class MLBStandingsAPI(BaseAPI[MLBStandings]):
    model_class = MLBStandings

    def get(self, season: int) -> ListResponse[MLBStandings]:
        return self._get_list("mlb/v1/standings", {"season": season})

class MLBPlayerInjuriesAPI(BaseAPI[MLBPlayerInjury]):
    model_class = MLBPlayerInjury

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None
    ) -> PaginatedListResponse[MLBPlayerInjury]:
        return self._get_paginated_list("mlb/v1/player_injuries", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids
        })

class MLBSeasonStatsAPI(BaseAPI[MLBSeasonStats]):
    model_class = MLBSeasonStats

    def list(
        self,
        season: int,
        player_ids: Optional[List[int]] = None,
        team_id: Optional[int] = None,
        postseason: Optional[bool] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None
    ) -> PaginatedListResponse[MLBSeasonStats]:
        return self._get_paginated_list("mlb/v1/season_stats", {
            "season": season,
            "player_ids": player_ids,
            "team_id": team_id,
            "postseason": postseason,
            "sort_by": sort_by,
            "sort_order": sort_order
        })

class MLBTeamSeasonStatsAPI(BaseAPI[MLBTeamSeasonStats]):
    model_class = MLBTeamSeasonStats

    def list(
        self,
        season: int,
        team_id: Optional[int] = None,
        postseason: Optional[bool] = None
    ) -> PaginatedListResponse[MLBTeamSeasonStats]:
        return self._get_paginated_list("mlb/v1/teams/season_stats", {
            "season": season,
            "team_id": team_id,
            "postseason": postseason
        })

class MLBApi:
    def __init__(self, client):
        self.teams = MLBTeamsAPI(client)
        self.players = MLBPlayersAPI(client)
        self.games = MLBGamesAPI(client)
        self.stats = MLBStatsAPI(client)
        self.standings = MLBStandingsAPI(client)
        self.injuries = MLBPlayerInjuriesAPI(client)
        self.season_stats = MLBSeasonStatsAPI(client)
        self.team_season_stats = MLBTeamSeasonStatsAPI(client)