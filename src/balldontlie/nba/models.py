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
    first_name: Optional[str]
    last_name: Optional[str]
    position: Optional[str]
    height: Optional[str]
    weight: Optional[str]
    jersey_number: Optional[str]
    college: Optional[str]
    country: Optional[str]
    draft_year: Optional[int]
    draft_round: Optional[int]
    draft_number: Optional[int]
    team: Optional[NBATeam] = None
    team_id: Optional[int] = None

class NBAGame(BaseModel):
    id: int
    date: str
    season: int
    status: str
    period: int
    time: Optional[str] 
    postseason: bool
    home_team_score: int
    visitor_team_score: int
    home_team: Optional[NBATeam] = None
    home_team_id: Optional[int] = None
    visitor_team: Optional[NBATeam] = None
    visitor_team_id: Optional[int] = None

class NBAStats(BaseModel):
    id: Optional[int] = None
    min: Optional[str]
    fgm: Optional[int]
    fga: Optional[int]
    fg_pct: Optional[float]
    fg3m: Optional[int]
    fg3a: Optional[int]
    fg3_pct: Optional[float]
    ftm: Optional[int]
    fta: Optional[int]
    ft_pct: Optional[float]
    oreb: Optional[int]
    dreb: Optional[int]
    reb: Optional[int]
    ast: Optional[int]
    stl: Optional[int]
    blk: Optional[int]
    turnover: Optional[int]
    pf: Optional[int]
    pts: Optional[int]
    player: NBAPlayer
    team: Optional[NBATeam] = None
    game: Optional[NBAGame] = None

class NBASeasonAverages(BaseModel):
    games_played: int
    pts: float
    ast: float
    reb: float
    stl: float
    blk: float
    turnover: float
    min: str
    fgm: float
    fga: float
    fg_pct: float
    fg3m: float
    fg3a: float
    fg3_pct: float
    ftm: float
    fta: float
    ft_pct: float
    oreb: float
    dreb: float
    player_id: int
    season: int

class NBAStandings(BaseModel):
    team: NBATeam
    conference_record: str
    conference_rank: int
    division_record: str
    division_rank: int
    wins: int
    losses: int
    home_record: str
    road_record: str
    season: int

class NBABoxScoreTeam(NBATeam):
    players: List[NBAStats]

class NBABoxScore(BaseModel):
    date: str
    season: int
    status: str
    period: int
    time: Optional[str]
    postseason: bool
    home_team_score: int
    visitor_team_score: int
    home_team: NBABoxScoreTeam
    visitor_team: NBABoxScoreTeam

class NBAPlayerInjury(BaseModel):
    player: NBAPlayer
    return_date: Optional[str]
    description: str
    status: str

class NBALeader(BaseModel):
    player: NBAPlayer
    value: float
    stat_type: str
    rank: int
    season: int
    games_played: int

class NBAOdds(BaseModel):
    type: str
    vendor: str
    live: bool
    game_id: int
    odds_decimal_home: Optional[str]
    odds_decimal_visitor: Optional[str]
    odds_american_home: Optional[str]
    odds_american_visitor: Optional[str]
    away_spread: Optional[str] = None
    over_under: Optional[str] = None

class NBAAdvancedStats(BaseModel):
    id: int
    pie: float  # player impact estimate
    pace: float
    assist_percentage: float
    assist_ratio: float
    assist_to_turnover: float
    defensive_rating: float
    defensive_rebound_percentage: float
    effective_field_goal_percentage: float
    net_rating: float
    offensive_rating: float
    offensive_rebound_percentage: float
    rebound_percentage: float
    true_shooting_percentage: float
    turnover_ratio: float
    usage_percentage: float
    player: NBAPlayer
    team: NBATeam
    game: NBAGame