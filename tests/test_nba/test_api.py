import pytest

from balldontlie.exceptions import (
    AuthenticationError,
    NotFoundError,
)


def test_list_nba_teams(client):
    response = client.nba.teams.list()
    assert len(response.data) > 0
    team = response.data[0]
    assert team.id is not None
    assert team.name is not None
    assert team.conference in ["East", "West"]


def test_get_nba_team(client):
    response = client.nba.teams.get(1)
    team = response.data
    assert team.id == 1
    assert team.name is not None
    assert team.abbreviation is not None


def test_list_nba_players(client):
    response = client.nba.players.list(per_page=25)
    assert len(response.data) <= 25
    assert response.meta.per_page == 25
    assert response.meta.next_cursor is not None
    player = response.data[0]
    assert player.id is not None
    assert player.first_name is not None
    assert player.last_name is not None


def test_list_active_nba_players(client):
    response = client.nba.players.list_active(per_page=25)
    assert len(response.data) <= 25
    player = response.data[0]
    assert player.id is not None
    assert player.team is not None


def test_get_nba_player(client):
    response = client.nba.players.get(115)
    player = response.data
    assert player.id == 115
    assert player.first_name == "Stephen"
    assert player.last_name == "Curry"
    assert player.team is not None


def test_list_nba_games(client):
    response = client.nba.games.list(
        dates=["2024-04-01", "2024-04-02", "2024-04-03", "2024-04-04"], per_page=25
    )
    assert len(response.data) <= 25
    game = response.data[0]
    assert game.id is not None
    assert game.home_team is not None
    assert game.visitor_team is not None


def test_get_nba_game(client):
    response = client.nba.games.get(3277498)
    game = response.data
    assert game.id == 3277498
    assert game.home_team_score >= 0
    assert game.visitor_team_score >= 0


def test_list_nba_stats(client):
    response = client.nba.stats.list(per_page=25)
    assert len(response.data) <= 25
    assert response.meta.per_page == 25
    assert response.meta.next_cursor is not None
    stats = response.data[0]
    assert stats.id is not None
    assert stats.player is not None
    assert stats.game is not None


def test_get_nba_season_averages(client):
    response = client.nba.season_averages.get(season=2023, player_id=115)
    stats = response.data[0]
    assert stats.season == 2023
    assert stats.games_played >= 0


def test_get_nba_standings(client):
    response = client.nba.standings.get(season=2024)
    assert len(response.data) > 0
    standing = response.data[0]
    assert standing.team is not None
    assert standing.wins >= 0
    assert standing.losses >= 0


def test_get_live_box_scores(client):
    response = client.nba.box_scores.get_live()
    for box_score in response.data:
        assert box_score.home_team is not None
        assert box_score.visitor_team is not None


def test_get_box_scores_by_date(client):
    response = client.nba.box_scores.get_by_date(date="2024-11-26")
    for box_score in response.data:
        assert box_score.home_team is not None


def test_list_nba_injuries(client):
    response = client.nba.injuries.list(per_page=25)
    assert len(response.data) <= 25
    if response.data:
        injury = response.data[0]
        assert injury.player is not None
        assert injury.status is not None


def test_get_nba_leaders(client):
    response = client.nba.leaders.get(stat_type="pts", season=2023)
    assert len(response.data) > 0
    leader = response.data[0]
    assert leader.player is not None
    assert leader.value > 0
    assert leader.rank > 0


def test_nba_advanced_stats(client):
    response = client.nba.advanced_stats.list(per_page=25)
    assert len(response.data) <= 25
    stats = response.data[0]
    assert stats.player is not None
    assert stats.team is not None
    assert stats.game is not None


def test_nba_odds(client):
    response = client.nba.odds.list(date="2024-11-26")
    assert len(response.data) > 0
    odds = response.data[0]
    assert odds.type is not None
    assert odds.vendor is not None
    assert odds.live is not None


def test_authentication_error(client):
    client.api_key = "invalid_key"
    with pytest.raises(AuthenticationError) as exc_info:
        client.nba.teams.list()
    assert exc_info.value.status_code == 401


def test_not_found_error(client):
    with pytest.raises(NotFoundError) as exc_info:
        client.nba.teams.get(99999)
    assert exc_info.value.status_code == 404
