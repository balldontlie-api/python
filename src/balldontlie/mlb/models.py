from typing import Optional, List
from pydantic import BaseModel


class MLBTeam(BaseModel):
    id: int
    slug: str
    abbreviation: str
    display_name: str
    short_display_name: str
    name: str
    location: str
    league: str
    division: str


class MLBPlayer(BaseModel):
    id: int
    first_name: str
    last_name: str
    full_name: str
    debut_year: Optional[int]
    jersey: Optional[str]
    college: Optional[str]
    position: Optional[str]
    active: Optional[bool]
    birth_place: Optional[str]
    dob: Optional[str]
    age: Optional[int]
    height: Optional[str]
    weight: Optional[str]
    draft: Optional[str]
    bats_throws: Optional[str]
    team: Optional[MLBTeam] = None


class MLBGameTeamData(BaseModel):
    hits: int
    runs: int
    errors: int
    inning_scores: List[int]


class MLBGameScoringSummary(BaseModel):
    play: str
    inning: str
    period: str
    away_score: int
    home_score: int


class MLBGame(BaseModel):
    id: int
    home_team_name: str
    away_team_name: str
    home_team: MLBTeam
    away_team: MLBTeam
    season: int
    postseason: bool
    date: str
    home_team_data: Optional[MLBGameTeamData]
    away_team_data: Optional[MLBGameTeamData]
    venue: Optional[str]
    attendance: Optional[int]
    status: Optional[str]
    conference_play: Optional[bool]
    period: Optional[int]
    clock: Optional[int]
    display_clock: Optional[str]
    scoring_summary: Optional[List[MLBGameScoringSummary]]


class MLBStats(BaseModel):
    player: MLBPlayer
    game: MLBGame
    team_name: str
    at_bats: Optional[int]
    runs: Optional[int]
    hits: Optional[int]
    rbi: Optional[int]
    hr: Optional[int]
    bb: Optional[int]
    k: Optional[int]
    avg: Optional[float]
    obp: Optional[float]
    slg: Optional[float]
    ip: Optional[float]
    p_hits: Optional[int]
    p_runs: Optional[int]
    er: Optional[int]
    p_bb: Optional[int]
    p_k: Optional[int]
    p_hr: Optional[int]
    pitch_count: Optional[int]
    strikes: Optional[int]
    era: Optional[float]


class MLBStandings(BaseModel):
    season: int
    team: MLBTeam
    league_name: str
    league_short_name: str
    division_name: str
    division_short_name: str
    team_name: str
    ot_losses: int
    ot_wins: int
    avg_points_against: float
    avg_points_for: float
    clincher: Optional[str]
    differential: Optional[float]
    division_win_percent: Optional[float]
    games_behind: Optional[int]
    games_played: Optional[int]
    league_win_percent: Optional[float]
    losses: Optional[int]
    playoff_seed: Optional[int]
    point_differential: Optional[int]
    game_back_points: Optional[int]
    points_against: Optional[int]
    points_for: Optional[int]
    streak: Optional[int]
    ties: Optional[int]
    win_percent: Optional[float]
    wins: Optional[int]
    division_games_behind: Optional[int]
    division_percent: Optional[int]
    division_tied: Optional[int]
    home_losses: Optional[int]
    home_ties: Optional[int]
    home_wins: Optional[int]
    magic_number_division: Optional[int]
    magic_number_wildcard: Optional[int]
    playoff_percent: Optional[int]
    road_losses: Optional[int]
    road_ties: Optional[int]
    road_wins: Optional[int]
    wildcard_percent: Optional[float]
    total: Optional[str]
    home: Optional[str]
    road: Optional[str]
    intra_division: Optional[str]
    intra_league: Optional[str]
    last_ten_games: Optional[str]


class MLBSeasonStats(BaseModel):
    player: MLBPlayer
    team_name: str
    season: int
    postseason: bool
    batting_gp: Optional[int]
    batting_ab: Optional[int]
    batting_r: Optional[int]
    batting_h: Optional[int]
    batting_avg: Optional[float]
    batting_2b: Optional[int]
    batting_3b: Optional[int]
    batting_hr: Optional[int]
    batting_rbi: Optional[int]
    batting_bb: Optional[int]
    batting_so: Optional[int]
    batting_sb: Optional[int]
    batting_obp: Optional[float]
    batting_slg: Optional[float]
    batting_ops: Optional[float]
    batting_war: Optional[float]
    pitching_gp: Optional[int]
    pitching_gs: Optional[int]
    pitching_w: Optional[int]
    pitching_l: Optional[int]
    pitching_era: Optional[float]
    pitching_sv: Optional[int]
    pitching_ip: Optional[float]
    pitching_h: Optional[int]
    pitching_er: Optional[int]
    pitching_hr: Optional[int]
    pitching_bb: Optional[int]
    pitching_k: Optional[int]
    pitching_war: Optional[float]
    fielding_gp: Optional[int]
    fielding_gs: Optional[int]
    fielding_fip: Optional[float]
    fielding_tc: Optional[int]
    fielding_po: Optional[int]
    fielding_a: Optional[int]
    fielding_fp: Optional[float]
    fielding_e: Optional[int]
    fielding_dp: Optional[int]
    fielding_rf: Optional[float]
    fielding_dwar: Optional[float]
    fielding_pb: Optional[int]
    fielding_cs: Optional[int]
    fielding_cs_percent: Optional[float]
    fielding_sba: Optional[int]


class MLBTeamSeasonStats(BaseModel):
    team: MLBTeam
    team_name: str
    postseason: bool
    season: int
    gp: Optional[int] = None
    batting_ab: Optional[int] = None
    batting_r: Optional[int] = None
    batting_h: Optional[int] = None
    batting_2b: Optional[int] = None
    batting_3b: Optional[int] = None
    batting_hr: Optional[int] = None
    batting_rbi: Optional[int] = None
    batting_tb: Optional[int] = None
    batting_bb: Optional[int] = None
    batting_so: Optional[int] = None
    batting_sb: Optional[int] = None
    batting_avg: Optional[float] = None
    batting_obp: Optional[float] = None
    batting_slg: Optional[float] = None
    batting_ops: Optional[float] = None
    pitching_w: Optional[int] = None
    pitching_l: Optional[int] = None
    pitching_era: Optional[float] = None
    pitching_sv: Optional[int] = None
    pitching_cg: Optional[int] = None
    pitching_sho: Optional[int] = None
    pitching_qs: Optional[int] = None
    pitching_ip: Optional[float] = None
    pitching_h: Optional[int] = None
    pitching_er: Optional[int] = None
    pitching_hr: Optional[int] = None
    pitching_bb: Optional[int] = None
    pitching_k: Optional[int] = None
    pitching_oba: Optional[float] = None
    pitching_whip: Optional[float] = None
    fielding_e: Optional[int] = None
    fielding_fp: Optional[float] = None
    fielding_tc: Optional[int] = None
    fielding_po: Optional[int] = None
    fielding_a: Optional[int] = None


class MLBPlayerInjury(BaseModel):
    player: MLBPlayer
    date: str
    return_date: Optional[str]
    type: Optional[str]
    detail: Optional[str]
    side: Optional[str]
    status: Optional[str]
    long_comment: Optional[str]
    short_comment: Optional[str]
