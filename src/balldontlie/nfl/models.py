from typing import Optional
from pydantic import BaseModel


class NFLTeam(BaseModel):
    id: int
    conference: str
    division: str
    location: str
    name: str
    full_name: str
    abbreviation: str


class NFLPlayer(BaseModel):
    id: int
    first_name: str
    last_name: str
    position: str
    position_abbreviation: str
    height: str
    weight: str
    jersey_number: Optional[str] = None
    college: Optional[str] = None
    experience: Optional[str] = None
    age: Optional[float] = None
    team: Optional[NFLTeam] = None
    team_id: Optional[float] = None


class NFLGame(BaseModel):
    id: int
    visitor_team: NFLTeam
    home_team: NFLTeam
    week: int
    date: str
    season: int
    postseason: bool
    status: str
    summary: Optional[str] = None
    venue: Optional[str] = None
    home_team_score: Optional[float] = None
    home_team_q1: Optional[float] = None
    home_team_q2: Optional[float] = None
    home_team_q3: Optional[float] = None
    home_team_q4: Optional[float] = None
    home_team_ot: Optional[float] = None
    visitor_team_score: Optional[float] = None
    visitor_team_q1: Optional[float] = None
    visitor_team_q2: Optional[float] = None
    visitor_team_q3: Optional[float] = None
    visitor_team_q4: Optional[float] = None
    visitor_team_ot: Optional[float] = None


class NFLStats(BaseModel):
    player: NFLPlayer
    team: NFLTeam
    game: NFLGame
    passing_completions: Optional[float] = None
    passing_attempts: Optional[float] = None
    passing_yards: Optional[float] = None
    yards_per_pass_attempt: Optional[float] = None
    passing_touchdowns: Optional[float] = None
    passing_interceptions: Optional[float] = None
    sacks: Optional[float] = None
    sacks_loss: Optional[float] = None
    qbr: Optional[float] = None
    qb_rating: Optional[float] = None
    rushing_attempts: Optional[float] = None
    rushing_yards: Optional[float] = None
    yards_per_rush_attempt: Optional[float] = None
    rushing_touchdowns: Optional[float] = None
    long_rushing: Optional[float] = None
    receptions: Optional[float] = None
    receiving_yards: Optional[float] = None
    yards_per_reception: Optional[float] = None
    receiving_touchdowns: Optional[float] = None
    long_reception: Optional[float] = None
    receiving_targets: Optional[float] = None
    fumbles: Optional[float] = None
    fumbles_lost: Optional[float] = None
    fumbles_recovered: Optional[float] = None
    total_tackles: Optional[float] = None
    defensive_sacks: Optional[float] = None
    solo_tackles: Optional[float] = None
    tackles_for_loss: Optional[float] = None
    passes_defended: Optional[float] = None
    qb_hits: Optional[float] = None
    fumbles_touchdowns: Optional[float] = None
    defensive_interceptions: Optional[float] = None
    interception_yards: Optional[float] = None
    interception_touchdowns: Optional[float] = None
    kick_returns: Optional[float] = None
    kick_return_yards: Optional[float] = None
    yards_per_kick_return: Optional[float] = None
    long_kick_return: Optional[float] = None
    kick_return_touchdowns: Optional[float] = None
    punt_returns: Optional[float] = None
    punt_return_yards: Optional[float] = None
    yards_per_punt_return: Optional[float] = None
    long_punt_return: Optional[float] = None
    punt_return_touchdowns: Optional[float] = None
    field_goal_attempts: Optional[float] = None
    field_goals_made: Optional[float] = None
    field_goal_pct: Optional[float] = None
    long_field_goal_made: Optional[float] = None
    extra_points_made: Optional[float] = None
    total_points: Optional[float] = None
    punts: Optional[float] = None
    punt_yards: Optional[float] = None
    gross_avg_punt_yards: Optional[float] = None
    touchbacks: Optional[float] = None
    punts_inside_20: Optional[float] = None
    long_punt: Optional[float] = None


class NFLStandings(BaseModel):
    team: NFLTeam
    season: int
    win_streak: Optional[float] = None
    points_for: Optional[float] = None
    points_against: Optional[float] = None
    playoff_seed: Optional[float] = None
    point_differential: Optional[float] = None
    overall_record: Optional[str] = None
    conference_record: Optional[str] = None
    division_record: Optional[str] = None
    wins: Optional[float] = None
    losses: Optional[float] = None
    ties: Optional[float] = None
    home_record: Optional[str] = None
    road_record: Optional[str] = None


class NFLPlayerInjury(BaseModel):
    player: NFLPlayer
    status: str
    comment: Optional[str] = None
    date: Optional[str] = None


class NFLSeasonStats(BaseModel):
    player: NFLPlayer
    games_played: int
    season: int
    postseason: bool
    passing_completions: Optional[float] = None
    passing_attempts: Optional[float] = None
    passing_yards: Optional[float] = None
    yards_per_pass_attempt: Optional[float] = None
    passing_touchdowns: Optional[float] = None
    passing_interceptions: Optional[float] = None
    passing_yards_per_game: Optional[float] = None
    passing_completion_pct: Optional[float] = None
    qbr: Optional[float] = None
    rushing_attempts: Optional[float] = None
    rushing_yards: Optional[float] = None
    rushing_yards_per_game: Optional[float] = None
    yards_per_rush_attempt: Optional[float] = None
    rushing_touchdowns: Optional[float] = None
    rushing_fumbles: Optional[float] = None
    rushing_fumbles_lost: Optional[float] = None
    rushing_first_downs: Optional[float] = None
    receptions: Optional[float] = None
    receiving_yards: Optional[float] = None
    yards_per_reception: Optional[float] = None
    receiving_touchdowns: Optional[float] = None
    receiving_fumbles: Optional[float] = None
    receiving_fumbles_lost: Optional[float] = None
    receiving_first_downs: Optional[float] = None
    receiving_targets: Optional[float] = None
    receiving_yards_per_game: Optional[float] = None
    fumbles_forced: Optional[float] = None
    fumbles_recovered: Optional[float] = None
    total_tackles: Optional[float] = None
    defensive_sacks: Optional[float] = None
    defensive_sack_yards: Optional[float] = None
    solo_tackles: Optional[float] = None
    assist_tackles: Optional[float] = None
    fumbles_touchdowns: Optional[float] = None
    defensive_interceptions: Optional[float] = None
    interception_touchdowns: Optional[float] = None
    kick_returns: Optional[float] = None
    kick_return_yards: Optional[float] = None
    yards_per_kick_return: Optional[float] = None
    kick_return_touchdowns: Optional[float] = None
    punt_returner_returns: Optional[float] = None
    punt_returner_return_yards: Optional[float] = None
    yards_per_punt_return: Optional[float] = None
    punt_return_touchdowns: Optional[float] = None
    field_goal_attempts: Optional[float] = None
    field_goals_made: Optional[float] = None
    field_goal_pct: Optional[float] = None
    punts: Optional[float] = None
    punt_yards: Optional[float] = None
    field_goals_made_1_19: Optional[float] = None
    field_goals_made_20_29: Optional[float] = None
    field_goals_made_30_39: Optional[float] = None
    field_goals_made_40_49: Optional[float] = None
    field_goals_made_50: Optional[float] = None
    field_goals_attempts_1_19: Optional[float] = None
    field_goals_attempts_20_29: Optional[float] = None
    field_goals_attempts_30_39: Optional[float] = None
    field_goals_attempts_40_49: Optional[float] = None
    field_goals_attempts_50: Optional[float] = None


class NFLAdvancedRushingStats(BaseModel):
    player: NFLPlayer
    season: int
    week: int
    avg_time_to_los: Optional[float] = None
    expected_rush_yards: Optional[float] = None
    rush_attempts: Optional[float] = None
    rush_pct_over_expected: Optional[float] = None
    rush_touchdowns: Optional[float] = None
    rush_yards: Optional[float] = None
    rush_yards_over_expected: Optional[float] = None
    rush_yards_over_expected_per_att: Optional[float] = None
    efficiency: Optional[float] = None
    percent_attempts_gte_eight_defenders: Optional[float] = None
    avg_rush_yards: Optional[float] = None


class NFLAdvancedPassingStats(BaseModel):
    player: NFLPlayer
    season: int
    week: int
    aggressiveness: Optional[float] = None
    attempts: Optional[float] = None
    avg_air_distance: Optional[float] = None
    avg_air_yards_differential: Optional[float] = None
    avg_air_yards_to_sticks: Optional[float] = None
    avg_completed_air_yards: Optional[float] = None
    avg_intended_air_yards: Optional[float] = None
    avg_time_to_throw: Optional[float] = None
    completion_percentage: Optional[float] = None
    completion_percentage_above_expectation: Optional[float] = None
    completions: Optional[float] = None
    expected_completion_percentage: Optional[float] = None
    games_played: Optional[float] = None
    interceptions: Optional[float] = None
    max_air_distance: Optional[float] = None
    max_completed_air_distance: float = None
    pass_touchdowns: Optional[float] = None
    pass_yards: Optional[float] = None
    passer_rating: Optional[float] = None


class NFLAdvancedReceivingStats(BaseModel):
    player: NFLPlayer
    season: int
    week: int
    avg_cushion: Optional[float] = None
    avg_expected_yac: Optional[float] = None
    avg_intended_air_yards: Optional[float] = None
    avg_separation: Optional[float] = None
    avg_yac: Optional[float] = None
    avg_yac_above_expectation: Optional[float] = None
    catch_percentage: Optional[float] = None
    percent_share_of_intended_air_yards: Optional[float] = None
    rec_touchdowns: Optional[float] = None
    receptions: Optional[float] = None
    targets: Optional[float] = None
    yards: Optional[float] = None
