from typing import Optional, List
from ..base import BaseAPI, BaseResponse, ListResponse, PaginatedListResponse
from .models import *

class NBATeamsAPI(BaseAPI[NBATeam]):
    model_class = NBATeam

    def list(
        self, 
        division: Optional[str] = None, 
        conference: Optional[str] = None
    ) -> ListResponse[NBATeam]:
        return self._get_list("nba/v1/teams", {
            "division": division,
            "conference": conference
        })

    def get(self, team_id: int) -> BaseResponse[NBATeam]:
        return self._get_data(f"nba/v1/teams/{team_id}")

class NBAPlayersAPI(BaseAPI[NBAPlayer]):
    model_class = NBAPlayer

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ) -> PaginatedListResponse[NBAPlayer]:
        return self._get_paginated_list("nba/v1/players", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids,
            "search": search,
            "first_name": first_name,
            "last_name": last_name
        })

    def get(self, player_id: int) -> BaseResponse[NBAPlayer]:
        return self._get_data(f"nba/v1/players/{player_id}")

    def list_active(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None,
        search: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ) -> PaginatedListResponse[NBAPlayer]:
        return self._get_paginated_list("nba/v1/players/active", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids,
            "search": search,
            "first_name": first_name,
            "last_name": last_name
        })

class NBAGamesAPI(BaseAPI[NBAGame]):
    model_class = NBAGame

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        dates: Optional[List[str]] = None,
        team_ids: Optional[List[int]] = None,
        seasons: Optional[List[int]] = None,
        postseason: Optional[bool] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> PaginatedListResponse[NBAGame]:
        return self._get_paginated_list("nba/v1/games", {
            "cursor": cursor,
            "per_page": per_page,
            "dates": dates,
            "team_ids": team_ids,
            "seasons": seasons,
            "postseason": postseason,
            "start_date": start_date,
            "end_date": end_date
        })

    def get(self, game_id: int) -> BaseResponse[NBAGame]:
        return self._get_data(f"nba/v1/games/{game_id}")

class NBAStatsAPI(BaseAPI[NBAStats]):
    model_class = NBAStats

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        player_ids: Optional[List[int]] = None,
        game_ids: Optional[List[int]] = None,
        dates: Optional[List[str]] = None,
        seasons: Optional[List[int]] = None,
        postseason: Optional[bool] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> PaginatedListResponse[NBAStats]:
        return self._get_paginated_list("nba/v1/stats", {
            "cursor": cursor,
            "per_page": per_page,
            "player_ids": player_ids,
            "game_ids": game_ids,
            "dates": dates,
            "seasons": seasons,
            "postseason": postseason,
            "start_date": start_date,
            "end_date": end_date
        })

class NBASeasonAveragesAPI(BaseAPI[NBASeasonAverages]):
    model_class = NBASeasonAverages

    def get(self, season: int, player_id: int) -> ListResponse[NBASeasonAverages]:
        return self._get_list("nba/v1/season_averages", {
            "season": season,
            "player_id": player_id
        })

class NBAStandingsAPI(BaseAPI[NBAStandings]):
    model_class = NBAStandings

    def get(self, season: int) -> ListResponse[NBAStandings]:
        return self._get_list("nba/v1/standings", {
            "season": season
        })

class NBABoxScoresAPI(BaseAPI[NBABoxScore]):
    model_class = NBABoxScore

    def get_live(self) -> ListResponse[NBABoxScore]:
        return self._get_list("nba/v1/box_scores/live")

    def get_by_date(self, date: str) -> ListResponse[NBABoxScore]:
        return self._get_list("nba/v1/box_scores", {
            "date": date
        })

class NBAPlayerInjuriesAPI(BaseAPI[NBAPlayerInjury]):
    model_class = NBAPlayerInjury

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        team_ids: Optional[List[int]] = None,
        player_ids: Optional[List[int]] = None
    ) -> PaginatedListResponse[NBAPlayerInjury]:
        return self._get_paginated_list("nba/v1/player_injuries", {
            "cursor": cursor,
            "per_page": per_page,
            "team_ids": team_ids,
            "player_ids": player_ids
        })

class NBALeadersAPI(BaseAPI[NBALeader]):
    model_class = NBALeader

    def get(self, stat_type: str, season: int) -> ListResponse[NBALeader]:
        return self._get_list("nba/v1/leaders", {
            "stat_type": stat_type,
            "season": season
        })

class NBAOddsAPI(BaseAPI[NBAOdds]):
    model_class = NBAOdds

    def list(
        self, 
        date: Optional[str] = None, 
        game_id: Optional[int] = None
    ) -> ListResponse[NBAOdds]:
        return self._get_list("nba/v1/odds", {
            "date": date,
            "game_id": game_id
        })

class NBAAdvancedStatsAPI(BaseAPI[NBAAdvancedStats]):
    model_class = NBAAdvancedStats

    def list(
        self,
        cursor: Optional[int] = None,
        per_page: Optional[int] = 25,
        player_ids: Optional[List[int]] = None,
        game_ids: Optional[List[int]] = None,
        dates: Optional[List[str]] = None,
        seasons: Optional[List[int]] = None,
        postseason: Optional[bool] = None
    ) -> PaginatedListResponse[NBAAdvancedStats]:
        return self._get_paginated_list("nba/v1/stats/advanced", {
            "cursor": cursor,
            "per_page": per_page,
            "player_ids": player_ids,
            "game_ids": game_ids,
            "dates": dates,
            "seasons": seasons,
            "postseason": postseason
        })

class NBAApi:
    def __init__(self, client):
        self.teams = NBATeamsAPI(client)
        self.players = NBAPlayersAPI(client)
        self.games = NBAGamesAPI(client)
        self.stats = NBAStatsAPI(client)
        self.season_averages = NBASeasonAveragesAPI(client)
        self.standings = NBAStandingsAPI(client)
        self.box_scores = NBABoxScoresAPI(client)
        self.injuries = NBAPlayerInjuriesAPI(client)
        self.leaders = NBALeadersAPI(client)
        self.odds = NBAOddsAPI(client)
        self.advanced_stats = NBAAdvancedStatsAPI(client)