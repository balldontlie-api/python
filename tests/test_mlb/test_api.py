import pytest


# def test_list_mlb_teams(client):
#     response = client.mlb.teams.list()
#     assert len(response.data) > 0
#     team = response.data[0]
#     assert team.id is not None
#     assert team.league in ["American", "National"]


# def test_get_mlb_team(client):
#     response = client.mlb.teams.get(6)
#     team = response.data
#     assert team.id == 6
#     assert team.name is not None


# def test_list_mlb_players(client):
#     response = client.mlb.players.list(per_page=25)
#     assert len(response.data) <= 25
#     player = response.data[0]
#     assert player.id is not None
#     assert player.position is not None


# def test_list_active_mlb_players(client):
#     response = client.mlb.players.list_active(per_page=25)
#     assert len(response.data) <= 25
#     player = response.data[0]
#     assert player.id is not None
#     assert player.active is True


# def test_get_mlb_player(client):
#     response = client.mlb.players.get(208)
#     player = response.data
#     assert player.id == 208
#     assert player.team is not None


# def test_list_mlb_games(client):
#     response = client.mlb.games.list(seasons=[2024], per_page=1)
#     assert len(response.data) > 0
#     game = response.data[0]
#     assert game.home_team is not None
#     assert game.away_team is not None


# def test_get_mlb_game(client):
#     response = client.mlb.games.get(58590)
#     game = response.data
#     assert game.id == 58590
#     assert game.home_team_data is not None
#     assert game.away_team_data is not None


# def test_list_mlb_stats(client):
#     response = client.mlb.stats.list(per_page=25)
#     assert len(response.data) <= 25
#     if response.data:
#         stats = response.data[0]
#         assert stats.player is not None
#         assert stats.game is not None


# def test_get_mlb_standings(client):
#     response = client.mlb.standings.get(season=2024)
#     assert len(response.data) > 0
#     standing = response.data[0]
#     assert standing.team is not None
#     assert standing.wins >= 0


# def test_list_mlb_injuries(client):
#     response = client.mlb.injuries.list(per_page=25)
#     assert len(response.data) <= 25
#     if response.data:
#         injury = response.data[0]
#         assert injury.player is not None
#         assert injury.status is not None


# def test_list_mlb_season_stats(client):
#     response = client.mlb.season_stats.list(season=2024)
#     if response.data:
#         stats = response.data[0]
#         assert stats.player is not None
#         assert stats.season == 2024


def test_list_mlb_team_season_stats(client):
    response = client.mlb.team_season_stats.list(season=2024)
    if response.data:
        stats = response.data[0]
        assert stats.team is not None
        assert stats.season == 2024
