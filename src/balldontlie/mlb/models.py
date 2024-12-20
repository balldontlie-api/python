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
    debut_year: Optional[float] = None
    jersey: Optional[str] = None
    college: Optional[str] = None
    position: Optional[str] = None
    active: Optional[bool] = None
    birth_place: Optional[str] = None
    dob: Optional[str] = None
    age: Optional[float] = None
    height: Optional[str] = None
    weight: Optional[str] = None
    draft: Optional[str] = None
    bats_throws: Optional[str] = None
    team: Optional[MLBTeam] = None


class MLBGameTeamData(BaseModel):
    hits: Optional[float] = None
    runs: Optional[float] = None
    errors: Optional[float] = None
    inning_scores: Optional[List[int]] = None


class MLBGameScoringSummary(BaseModel):
    play: str
    inning: str
    period: str
    away_score: Optional[float] = None
    home_score: Optional[float] = None


class MLBGame(BaseModel):
    id: int
    home_team_name: str
    away_team_name: str
    home_team: MLBTeam
    away_team: MLBTeam
    season: int
    postseason: bool
    date: str
    home_team_data: Optional[MLBGameTeamData] = None
    away_team_data: Optional[MLBGameTeamData] = None
    venue: Optional[str] = None
    attendance: Optional[float] = None
    status: Optional[str] = None
    conference_play: Optional[bool] = None
    period: Optional[float] = None
    clock: Optional[float] = None
    display_clock: Optional[str] = None
    scoring_summary: Optional[List[MLBGameScoringSummary]] = None


class MLBStats(BaseModel):
    player: MLBPlayer
    game: MLBGame
    team_name: str
    at_bats: Optional[float] = None
    runs: Optional[float] = None
    hits: Optional[float] = None
    rbi: Optional[float] = None
    hr: Optional[float] = None
    bb: Optional[float] = None
    k: Optional[float] = None
    avg: Optional[float] = None
    obp: Optional[float] = None
    slg: Optional[float] = None
    ip: Optional[float] = None
    p_hits: Optional[float] = None
    p_runs: Optional[float] = None
    er: Optional[float] = None
    p_bb: Optional[float] = None
    p_k: Optional[float] = None
    p_hr: Optional[float] = None
    pitch_count: Optional[float] = None
    strikes: Optional[float] = None
    era: Optional[float] = None


class MLBStandings(BaseModel):
    season: int
    team: MLBTeam
    league_name: str
    league_short_name: str
    division_name: str
    division_short_name: str
    team_name: str
    ot_losses: Optional[float] = None
    ot_wins: Optional[float] = None
    avg_points_against: Optional[float] = None
    avg_points_for: Optional[float] = None
    clincher: Optional[str] = None
    differential: Optional[float] = None
    division_win_percent: Optional[float] = None
    games_behind: Optional[float] = None
    games_played: Optional[float] = None
    league_win_percent: Optional[float] = None
    losses: Optional[float] = None
    playoff_seed: Optional[float] = None
    point_differential: Optional[float] = None
    game_back_points: Optional[float] = None
    points_against: Optional[float] = None
    points_for: Optional[float] = None
    streak: Optional[float] = None
    ties: Optional[float] = None
    win_percent: Optional[float] = None
    wins: Optional[float] = None
    division_games_behind: Optional[float] = None
    division_percent: Optional[float] = None
    division_tied: Optional[float] = None
    home_losses: Optional[float] = None
    home_ties: Optional[float] = None
    home_wins: Optional[float] = None
    magic_number_division: Optional[float] = None
    magic_number_wildcard: Optional[float] = None
    playoff_percent: Optional[float] = None
    road_losses: Optional[float] = None
    road_ties: Optional[float] = None
    road_wins: Optional[float] = None
    wildcard_percent: Optional[float] = None
    total: Optional[str] = None
    home: Optional[str] = None
    road: Optional[str] = None
    intra_division: Optional[str] = None
    intra_league: Optional[str] = None
    last_ten_games: Optional[str] = None


class MLBSeasonStats(BaseModel):
    player: MLBPlayer
    team_name: str
    season: int
    postseason: bool
    batting_gp: Optional[float] = None
    batting_ab: Optional[float] = None
    batting_r: Optional[float] = None
    batting_h: Optional[float] = None
    batting_avg: Optional[float] = None
    batting_2b: Optional[float] = None
    batting_3b: Optional[float] = None
    batting_hr: Optional[float] = None
    batting_rbi: Optional[float] = None
    batting_bb: Optional[float] = None
    batting_so: Optional[float] = None
    batting_sb: Optional[float] = None
    batting_obp: Optional[float] = None
    batting_slg: Optional[float] = None
    batting_ops: Optional[float] = None
    batting_war: Optional[float] = None
    pitching_gp: Optional[float] = None
    pitching_gs: Optional[float] = None
    pitching_w: Optional[float] = None
    pitching_l: Optional[float] = None
    pitching_era: Optional[float] = None
    pitching_sv: Optional[float] = None
    pitching_ip: Optional[float] = None
    pitching_h: Optional[float] = None
    pitching_er: Optional[float] = None
    pitching_hr: Optional[float] = None
    pitching_bb: Optional[float] = None
    pitching_k: Optional[float] = None
    pitching_war: Optional[float] = None
    fielding_gp: Optional[float] = None
    fielding_gs: Optional[float] = None
    fielding_fip: Optional[float] = None
    fielding_tc: Optional[float] = None
    fielding_po: Optional[float] = None
    fielding_a: Optional[float] = None
    fielding_fp: Optional[float] = None
    fielding_e: Optional[float] = None
    fielding_dp: Optional[float] = None
    fielding_rf: Optional[float] = None
    fielding_dwar: Optional[float] = None
    fielding_pb: Optional[float] = None
    fielding_cs: Optional[float] = None
    fielding_cs_percent: Optional[float] = None
    fielding_sba: Optional[float] = None


class MLBTeamSeasonStats(BaseModel):
    team: MLBTeam
    team_name: str
    postseason: bool
    season: int
    gp: Optional[float] = None
    batting_ab: Optional[float] = None
    batting_r: Optional[float] = None
    batting_h: Optional[float] = None
    batting_2b: Optional[float] = None
    batting_3b: Optional[float] = None
    batting_hr: Optional[float] = None
    batting_rbi: Optional[float] = None
    batting_tb: Optional[float] = None
    batting_bb: Optional[float] = None
    batting_so: Optional[float] = None
    batting_sb: Optional[float] = None
    batting_avg: Optional[float] = None
    batting_obp: Optional[float] = None
    batting_slg: Optional[float] = None
    batting_ops: Optional[float] = None
    pitching_w: Optional[float] = None
    pitching_l: Optional[float] = None
    pitching_era: Optional[float] = None
    pitching_sv: Optional[float] = None
    pitching_cg: Optional[float] = None
    pitching_sho: Optional[float] = None
    pitching_qs: Optional[float] = None
    pitching_ip: Optional[float] = None
    pitching_h: Optional[float] = None
    pitching_er: Optional[float] = None
    pitching_hr: Optional[float] = None
    pitching_bb: Optional[float] = None
    pitching_k: Optional[float] = None
    pitching_oba: Optional[float] = None
    pitching_whip: Optional[float] = None
    fielding_e: Optional[float] = None
    fielding_fp: Optional[float] = None
    fielding_tc: Optional[float] = None
    fielding_po: Optional[float] = None
    fielding_a: Optional[float] = None


class MLBPlayerInjury(BaseModel):
    player: MLBPlayer
    date: Optional[str] = None
    return_date: Optional[str] = None
    type: Optional[str] = None
    detail: Optional[str] = None
    side: Optional[str] = None
    status: Optional[str] = None
    long_comment: Optional[str] = None
    short_comment: Optional[str] = None
