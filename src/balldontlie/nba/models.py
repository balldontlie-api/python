from typing import Optional, List
from pydantic import BaseModel


class NBATeam(BaseModel):
    id: int
    conference: str
    division: str
    city: str
    name: str
    full_name: str
    abbreviation: str


class NBAPlayer(BaseModel):
    id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[str] = None
    jersey_number: Optional[str] = None
    college: Optional[str] = None
    country: Optional[str] = None
    draft_year: Optional[float] = None
    draft_round: Optional[float] = None
    draft_number: Optional[float] = None
    team: Optional[NBATeam] = None
    team_id: Optional[float] = None


class NBAGame(BaseModel):
    id: int
    date: str
    season: int
    status: Optional[str] = None
    period: Optional[float] = None
    time: Optional[str] = None
    postseason: bool
    home_team_score: Optional[float] = None
    visitor_team_score: Optional[float] = None
    home_team: Optional[NBATeam] = None
    home_team_id: Optional[float] = None
    visitor_team: Optional[NBATeam] = None
    visitor_team_id: Optional[float] = None


class NBAStats(BaseModel):
    id: Optional[float] = None
    min: Optional[str] = None
    fgm: Optional[float] = None
    fga: Optional[float] = None
    fg_pct: Optional[float] = None
    fg3m: Optional[float] = None
    fg3a: Optional[float] = None
    fg3_pct: Optional[float] = None
    ftm: Optional[float] = None
    fta: Optional[float] = None
    ft_pct: Optional[float] = None
    oreb: Optional[float] = None
    dreb: Optional[float] = None
    reb: Optional[float] = None
    ast: Optional[float] = None
    stl: Optional[float] = None
    blk: Optional[float] = None
    turnover: Optional[float] = None
    pf: Optional[float] = None
    pts: Optional[float] = None
    player: NBAPlayer = None
    team: Optional[NBATeam] = None
    game: Optional[NBAGame] = None


class NBASeasonAverages(BaseModel):
    player_id: int
    season: int
    games_played: Optional[float] = None
    pts: Optional[float] = None
    ast: Optional[float] = None
    reb: Optional[float] = None
    stl: Optional[float] = None
    blk: Optional[float] = None
    turnover: Optional[float] = None
    min: Optional[str] = None
    fgm: Optional[float] = None
    fga: Optional[float] = None
    fg_pct: Optional[float] = None
    fg3m: Optional[float] = None
    fg3a: Optional[float] = None
    fg3_pct: Optional[float] = None
    ftm: Optional[float] = None
    fta: Optional[float] = None
    ft_pct: Optional[float] = None
    oreb: Optional[float] = None
    dreb: Optional[float] = None


class NBAStandings(BaseModel):
    season: int
    team: NBATeam
    conference_record: Optional[str] = None
    conference_rank: Optional[float] = None
    division_record: Optional[str] = None
    division_rank: Optional[float] = None
    wins: Optional[float] = None
    losses: Optional[float] = None
    home_record: Optional[str] = None
    road_record: Optional[str] = None


class NBABoxScoreTeam(NBATeam):
    players: Optional[List[NBAStats]] = None


class NBABoxScore(BaseModel):
    postseason: bool
    date: Optional[str] = None
    season: Optional[float] = None
    status: Optional[str] = None
    period: Optional[float] = None
    time: Optional[str] = None
    home_team_score: Optional[float] = None
    visitor_team_score: Optional[float] = None
    home_team: Optional[NBABoxScoreTeam] = None
    visitor_team: Optional[NBABoxScoreTeam] = None


class NBAPlayerInjury(BaseModel):
    player: NBAPlayer
    return_date: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class NBALeader(BaseModel):
    player: NBAPlayer
    value: Optional[float] = None
    stat_type: str
    rank: Optional[float] = None
    season: int
    games_played: Optional[float] = None


class NBAOdds(BaseModel):
    type: str
    vendor: str
    live: bool
    game_id: int
    odds_decimal_home: Optional[str] = None
    odds_decimal_visitor: Optional[str] = None
    odds_american_home: Optional[str] = None
    odds_american_visitor: Optional[str] = None
    away_spread: Optional[str] = None
    over_under: Optional[str] = None


class NBAAdvancedStats(BaseModel):
    id: int
    pie: Optional[float] = None
    pace: Optional[float] = None
    assist_percentage: Optional[float] = None
    assist_ratio: Optional[float] = None
    assist_to_turnover: Optional[float] = None
    defensive_rating: Optional[float] = None
    defensive_rebound_percentage: Optional[float] = None
    effective_field_goal_percentage: Optional[float] = None
    net_rating: Optional[float] = None
    offensive_rating: Optional[float] = None
    offensive_rebound_percentage: Optional[float] = None
    rebound_percentage: Optional[float] = None
    true_shooting_percentage: Optional[float] = None
    turnover_ratio: Optional[float] = None
    usage_percentage: Optional[float] = None
    player: NBAPlayer
    team: NBATeam
    game: NBAGame
