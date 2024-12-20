from typing import Optional, List, Literal, Union, Dict
from pydantic import BaseModel

PlayerStatType = Literal[
    "goals",
    "goal_assist",
    "clean_sheet",
    "appearances",
    "mins_played",
    "yellow_card",
    "red_card",
    "total_pass",
    "touches",
    "total_scoring_att",
    "hit_woodwork",
    "big_chance_missed",
    "total_offside",
    "total_tackle",
    "fouls",
    "dispossessed",
    "own_goals",
    "total_clearance",
    "clearance_off_line",
    "saves",
    "penalty_save",
    "total_high_claim",
    "punches",
]

TeamStatType = Literal[
    "wins",
    "losses",
    "touches",
    "own_goals",
    "total_yel_card",
    "total_red_card",
    "goals",
    "total_pass",
    "total_scoring_att",
    "total_offside",
    "hit_woodwork",
    "big_chance_missed",
    "total_tackle",
    "total_clearance",
    "clearance_off_line",
    "dispossessed",
    "clean_sheet",
    "saves",
    "penalty_save",
    "total_high_claim",
    "punches",
]


class EPLTeam(BaseModel):
    id: int
    name: Optional[str] = None
    short_name: Optional[str] = None
    abbr: Optional[str] = None
    city: Optional[str] = None
    stadium: Optional[str] = None


class EPLPlayer(BaseModel):
    id: int
    position: Optional[str] = None
    national_team: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    birth_date: Optional[str] = None
    age: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    team_ids: Optional[List[int]] = None


class EPLGameLineup(BaseModel):
    team_id: int
    player: EPLPlayer
    substitute: Optional[bool] = None
    captain: Optional[bool] = None
    position: Optional[str] = None
    shirt_number: Optional[float] = None
    sub_clock: Optional[float] = None
    sub_clock_display: Optional[str] = None


class EPLGameGoal(BaseModel):
    game_id: int
    scorer: EPLPlayer
    assister: Optional[EPLPlayer] = None
    clock: Optional[float] = None
    clock_display: Optional[str] = None
    phase: Optional[str] = None
    type: Optional[str] = None


class StatEntry(BaseModel):
    name: str
    value: Optional[Union[float, int]] = None


class TeamStatEntry(BaseModel):
    team_id: int
    stats: Optional[List[StatEntry]] = None


class PlayerStatEntry(BaseModel):
    team_id: int
    player_id: int
    stats: Optional[List[StatEntry]] = None


class EPLGameTeamStats(BaseModel):
    game_id: int
    teams: List[TeamStatEntry]


class EPLGamePlayerStats(BaseModel):
    game_id: int
    players: List[PlayerStatEntry]


class EPLGame(BaseModel):
    id: int
    week: Optional[float] = None
    kickoff: Optional[str] = None
    provisional_kickoff: Optional[str] = None
    home_team_id: int
    away_team_id: int
    home_score: Optional[float] = None
    away_score: Optional[float] = None
    status: Optional[str] = None
    season: int
    ground: Optional[str] = None
    clock: Optional[float] = None
    clock_display: Optional[str] = None
    extra_time: Optional[bool] = None


class EPLStanding(BaseModel):
    team: EPLTeam
    season: int
    position: Optional[float] = None
    form: Optional[str] = None
    home_played: Optional[float] = None
    home_drawn: Optional[float] = None
    home_won: Optional[float] = None
    home_lost: Optional[float] = None
    home_goals_against: Optional[float] = None
    home_goals_difference: Optional[float] = None
    home_goals_for: Optional[float] = None
    home_points: Optional[float] = None
    away_played: Optional[float] = None
    away_drawn: Optional[float] = None
    away_won: Optional[float] = None
    away_lost: Optional[float] = None
    away_goals_against: Optional[float] = None
    away_goals_difference: Optional[float] = None
    away_goals_for: Optional[float] = None
    away_points: Optional[float] = None
    overall_played: Optional[float] = None
    overall_drawn: Optional[float] = None
    overall_won: Optional[float] = None
    overall_lost: Optional[float] = None
    overall_goals_against: Optional[float] = None
    overall_goals_difference: Optional[float] = None
    overall_goals_for: Optional[float] = None
    overall_points: Optional[float] = None


class EPLPlayerSeasonStat(BaseModel):
    value: Optional[float] = None
    name: Optional[str] = None
    rank: Optional[float] = None
    season: int


class EPLTeamSeasonStat(BaseModel):
    season: int
    value: Optional[float] = None
    name: Optional[str] = None
    rank: Optional[float] = None


class EPLPlayerStatLeaders(BaseModel):
    player: EPLPlayer
    season: int
    value: Optional[float] = None
    name: Optional[str] = None
    rank: Optional[float] = None


class EPLTeamStatLeaders(BaseModel):
    team: EPLTeam
    season: int
    value: Optional[float] = None
    name: Optional[str] = None
    rank: Optional[float] = None
