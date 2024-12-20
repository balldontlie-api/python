from typing import Optional, List
from ..base import BaseAPI, BaseResponse, ListResponse, PaginatedListResponse
from .models import *


class EPLTeamsAPI(BaseAPI[EPLTeam]):
    def list(self, season: int) -> ListResponse[EPLTeam]:
        self.model_class = EPLTeam
        return self._get_list("epl/v1/teams", {"season": season})

    def get_players(self, team_id: int, season: int) -> ListResponse[EPLPlayer]:
        self.model_class = EPLPlayer
        return self._get_list(f"epl/v1/teams/{team_id}/players", {"season": season})

    def get_season_stats(
        self, team_id: int, season: int
    ) -> ListResponse[EPLTeamSeasonStat]:
        self.model_class = EPLTeamSeasonStat
        return self._get_list(
            f"epl/v1/teams/{team_id}/season_stats", {"season": season}
        )


class EPLPlayersAPI(BaseAPI[EPLPlayer]):
    model_class = EPLPlayer

    def list(
        self,
        season: int,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ) -> PaginatedListResponse[EPLPlayer]:
        return self._get_paginated_list(
            "epl/v1/players",
            {
                "season": season,
                "cursor": cursor,
                "per_page": per_page,
                "team_ids": team_ids,
                "player_ids": player_ids,
                "search": search,
                "first_name": first_name,
                "last_name": last_name,
            },
        )

    def get_season_stats(
        self, player_id: int, season: int
    ) -> ListResponse[EPLPlayerSeasonStat]:
        self.model_class = EPLPlayerSeasonStat
        return self._get_list(
            f"epl/v1/players/{player_id}/season_stats", {"season": season}
        )


class EPLGamesAPI(BaseAPI[EPLGame]):
    def list(
        self,
        season: int,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_id: Optional[int] = None,
        week: Optional[int] = None,
    ) -> PaginatedListResponse[EPLGame]:
        self.model_class = EPLGame
        return self._get_paginated_list(
            "epl/v1/games",
            {
                "season": season,
                "cursor": cursor,
                "per_page": per_page,
                "team_id": team_id,
                "week": week,
            },
        )

    def get_lineups(self, game_id: int) -> ListResponse[EPLGameLineup]:
        self.model_class = EPLGameLineup
        return self._get_list(f"epl/v1/games/{game_id}/lineups")

    def get_goals(self, game_id: int) -> ListResponse[EPLGameGoal]:
        self.model_class = EPLGameGoal
        return self._get_list(f"epl/v1/games/{game_id}/goals")

    def get_team_stats(self, game_id: int) -> BaseResponse[EPLGameTeamStats]:
        self.model_class = EPLGameTeamStats
        return self._get_data(f"epl/v1/games/{game_id}/team_stats")

    def get_player_stats(self, game_id: int) -> BaseResponse[EPLGamePlayerStats]:
        self.model_class = EPLGamePlayerStats
        return self._get_data(f"epl/v1/games/{game_id}/player_stats")


class EPLStandingsAPI(BaseAPI[EPLStanding]):
    model_class = EPLStanding

    def get(self, season: int) -> ListResponse[EPLStanding]:
        return self._get_list("epl/v1/standings", {"season": season})


class EPLLeadersAPI:
    def __init__(self, client):
        self.players = EPLPlayerStatLeadersAPI(client)
        self.teams = EPLTeamStatLeadersAPI(client)


class EPLPlayerStatLeadersAPI(BaseAPI[EPLPlayerStatLeaders]):
    model_class = EPLPlayerStatLeaders

    def list(
        self,
        season: int,
        type: PlayerStatType,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
    ) -> PaginatedListResponse[EPLPlayerStatLeaders]:
        return self._get_paginated_list(
            "epl/v1/player_stats/leaders",
            {"cursor": cursor, "per_page": per_page, "season": season, "type": type},
        )


class EPLTeamStatLeadersAPI(BaseAPI[EPLTeamStatLeaders]):
    model_class = EPLTeamStatLeaders

    def list(
        self,
        season: int,
        type: TeamStatType,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
    ) -> PaginatedListResponse[EPLTeamStatLeaders]:
        return self._get_paginated_list(
            "epl/v1/team_stats/leaders",
            {"cursor": cursor, "per_page": per_page, "season": season, "type": type},
        )


class EPLApi:
    def __init__(self, client):
        self.teams = EPLTeamsAPI(client)
        self.players = EPLPlayersAPI(client)
        self.games = EPLGamesAPI(client)
        self.standings = EPLStandingsAPI(client)
        self.leaders = EPLLeadersAPI(client)
