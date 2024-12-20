import pytest


def test_list_nfl_teams(client):
    response = client.nfl.teams.list()
    assert len(response.data) > 0
    team = response.data[0]
    assert team.id is not None
    assert team.conference in ["AFC", "NFC"]


def test_get_nfl_team(client):
    response = client.nfl.teams.get(18)
    team = response.data
    assert team.id == 18
    assert team.conference is not None
    assert team.division is not None


def test_list_nfl_players(client):
    response = client.nfl.players.list(per_page=25)
    assert len(response.data) <= 25
    assert response.meta.per_page == 25
    assert response.meta.next_cursor is not None
    player = response.data[0]
    assert player.id is not None
    assert player.position is not None


def test_list_active_nfl_players(client):
    response = client.nfl.players.list_active(per_page=25)
    assert len(response.data) <= 25
    player = response.data[0]
    assert player.id is not None
    assert player.team is not None


def test_get_nfl_player(client):
    response = client.nfl.players.get(33)
    player = response.data
    assert player.id == 33
    assert player.team is not None
    assert player.first_name == "Lamar"
    assert player.last_name == "Jackson"


def test_list_nfl_games(client):
    response = client.nfl.games.list(dates=["2024-11-29", "2024-11-28"])
    assert len(response.data) > 0
    game = response.data[0]
    assert game.home_team is not None
    assert game.visitor_team is not None


def test_get_nfl_game(client):
    response = client.nfl.games.get(7001)
    game = response.data
    assert game.id == 7001
    assert game.week is not None


def test_list_nfl_stats(client):
    response = client.nfl.stats.list(per_page=25)
    assert len(response.data) <= 25
    stats = response.data[0]
    assert stats.player is not None
    assert stats.game is not None


def test_get_nfl_standings(client):
    response = client.nfl.standings.get(season=2024)
    assert len(response.data) > 0
    standing = response.data[0]
    assert standing.team is not None
    assert standing.conference_record is not None


def test_list_nfl_injuries(client):
    response = client.nfl.injuries.list(per_page=25)
    assert len(response.data) <= 25
    injury = response.data[0]
    assert injury.player is not None
    assert injury.status is not None


def test_list_nfl_season_stats(client):
    response = client.nfl.season_stats.list(season=2024)
    assert len(response.data) > 0
    stats = response.data[0]
    assert stats.player is not None
    assert stats.season == 2024


def test_get_advanced_rushing_stats(client):
    response = client.nfl.advanced_stats.rushing.get(season=2024)
    print(response)
    stats = response.data[0]
    assert stats.player is not None
    assert stats.rush_yards is not None


def test_get_advanced_passing_stats(client):
    response = client.nfl.advanced_stats.passing.get(season=2024)
    stats = response.data[0]
    assert stats.player is not None
    assert stats.completions is not None


def test_get_advanced_receiving_stats(client):
    response = client.nfl.advanced_stats.receiving.get(season=2024)
    stats = response.data[0]
    assert stats.player is not None
    assert stats.receptions is not None
