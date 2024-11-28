from typing import Optional, List
from ..base import BaseAPI, BaseResponse, ListResponse, PaginatedListResponse
from .models import *

class NFLTeamsAPI(BaseAPI[NFLTeam]):
    model_class = NFLTeam

    def list(
        self, 
        division: Optional[str] = None, 
        conference: Optional[str] = None
    ) -> ListResponse[NFLTeam]:
        return self._get_list("nfl/v1/teams", {
            "division": division,
            "conference": conference
        })

    def get(self, team_id: int) -> BaseResponse[NFLTeam]:
        return self._get_data(f"nfl/v1/teams/{team_id}")

class NFLPlayersAPI(BaseAPI[NFLPlayer]):
    model_class = NFLPlayer

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ) -> PaginatedListResponse[NFLPlayer]:
        return self._get_paginated_list("nfl/v1/players", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids,
            "search": search,
            "first_name": first_name,
            "last_name": last_name
        })

    def get(self, player_id: int) -> BaseResponse[NFLPlayer]:
        return self._get_data(f"nfl/v1/players/{player_id}")

    def list_active(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ) -> PaginatedListResponse[NFLPlayer]:
        return self._get_paginated_list("nfl/v1/players/active", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids,
            "search": search,
            "first_name": first_name,
            "last_name": last_name
        })

class NFLGamesAPI(BaseAPI[NFLGame]):
    model_class = NFLGame

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        dates: Optional[List[str]] = None,
        team_ids: Optional[List[int]] = None,
        seasons: Optional[List[int]] = None,
        postseason: Optional[bool] = None,
        weeks: Optional[List[int]] = None
    ) -> PaginatedListResponse[NFLGame]:
        return self._get_paginated_list("nfl/v1/games", {
            "cursor": cursor,
            "per_page": per_page,
            "dates": dates,
            "team_ids": team_ids,
            "seasons": seasons,
            "postseason": postseason,
            "weeks": weeks
        })

    def get(self, game_id: int) -> BaseResponse[NFLGame]:
        return self._get_data(f"nfl/v1/games/{game_id}")

class NFLStatsAPI(BaseAPI[NFLStats]):
    model_class = NFLStats

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        player_ids: Optional[List[int]] = None,
        game_ids: Optional[List[int]] = None,
        seasons: Optional[List[int]] = None
    ) -> PaginatedListResponse[NFLStats]:
        return self._get_paginated_list("nfl/v1/stats", {
            "cursor": cursor,
            "per_page": per_page,
            "player_ids": player_ids,
            "game_ids": game_ids,
            "seasons": seasons
        })

class NFLStandingsAPI(BaseAPI[NFLStandings]):
    model_class = NFLStandings

    def get(self, season: int) -> ListResponse[NFLStandings]:
        return self._get_list("nfl/v1/standings", {
            "season": season
        })

class NFLPlayerInjuriesAPI(BaseAPI[NFLPlayerInjury]):
    model_class = NFLPlayerInjury

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None
    ) -> PaginatedListResponse[NFLPlayerInjury]:
        return self._get_paginated_list("nfl/v1/player_injuries", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids
        })

class NFLSeasonStatsAPI(BaseAPI[NFLSeasonStats]):
    model_class = NFLSeasonStats

    def list(
        self,
        season: int,
        player_ids: Optional[List[int]] = None,
        team_id: Optional[int] = None,
        postseason: Optional[bool] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None
    ) -> PaginatedListResponse[NFLSeasonStats]:
        return self._get_paginated_list("nfl/v1/season_stats", {
            "season": season,
            "player_ids": player_ids,
            "team_id": team_id,
            "postseason": postseason,
            "sort_by": sort_by,
            "sort_order": sort_order
        })

class NFLAdvancedRushingStatsAPI(BaseAPI[NFLAdvancedRushingStats]):
    model_class = NFLAdvancedRushingStats

    def get(
        self,
        season: int,
        player_id: Optional[int] = None,
        week: Optional[int] = None
    ) -> PaginatedListResponse[NFLAdvancedRushingStats]:
        return self._get_paginated_list("nfl/v1/advanced_stats/rushing", {
            "season": season,
            "player_id": player_id,
            "week": week
        })

class NFLAdvancedPassingStatsAPI(BaseAPI[NFLAdvancedPassingStats]):
    model_class = NFLAdvancedPassingStats

    def get(
        self,
        season: int,
        player_id: Optional[int] = None,
        week: Optional[int] = None
    ) -> PaginatedListResponse[NFLAdvancedPassingStats]:
        return self._get_paginated_list("nfl/v1/advanced_stats/passing", {
            "season": season,
            "player_id": player_id,
            "week": week
        })

class NFLAdvancedReceivingStatsAPI(BaseAPI[NFLAdvancedReceivingStats]):
    model_class = NFLAdvancedReceivingStats

    def get(
        self,
        season: int,
        player_id: Optional[int] = None,
        week: Optional[int] = None
    ) -> PaginatedListResponse[NFLAdvancedReceivingStats]:
        return self._get_paginated_list("nfl/v1/advanced_stats/receiving", {
            "season": season,
            "player_id": player_id,
            "week": week
        })

class NFLAdvancedStatsAPI:
    def __init__(self, client):
        self.rushing = NFLAdvancedRushingStatsAPI(client)
        self.passing = NFLAdvancedPassingStatsAPI(client)
        self.receiving = NFLAdvancedReceivingStatsAPI(client)

class NFLApi:
    def __init__(self, client):
        self.teams = NFLTeamsAPI(client)
        self.players = NFLPlayersAPI(client)
        self.games = NFLGamesAPI(client)
        self.stats = NFLStatsAPI(client)
        self.standings = NFLStandingsAPI(client)
        self.injuries = NFLPlayerInjuriesAPI(client)
        self.season_stats = NFLSeasonStatsAPI(client)
        self.advanced_stats = NFLAdvancedStatsAPI(client)