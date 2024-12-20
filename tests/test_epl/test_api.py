import pytest

# Son heung-min player id
PLAYER_ID = 295
TEAM_ID = 45


def test_list_epl_teams(client):
    response = client.epl.teams.list(season=2024)
    assert len(response.data) > 0
    team = response.data[0]
    assert team.id is not None
    assert team.name is not None
    assert team.stadium is not None


def test_get_team_players(client):
    response = client.epl.teams.get_players(team_id=TEAM_ID, season=2024)
    assert len(response.data) > 0
    player = response.data[0]
    assert player.id is not None
    assert player.name is not None


def test_get_team_season_stats(client):
    response = client.epl.teams.get_season_stats(team_id=TEAM_ID, season=2024)
    assert len(response.data) > 0
    stat = response.data[0]
    assert stat.value is not None
    assert stat.name is not None
    assert stat.rank is not None
    assert stat.season == 2024


def test_list_epl_players_pagination(client):
    # Test first page
    first_page = client.epl.players.list(season=2024, per_page=5)
    assert len(first_page.data) == 5
    assert first_page.meta.per_page == 5
    assert first_page.meta.next_cursor is not None
    first_ids = {p.id for p in first_page.data}

    # Test second page
    second_page = client.epl.players.list(
        season=2024, per_page=5, cursor=first_page.meta.next_cursor
    )
    assert len(second_page.data) == 5
    assert second_page.meta.per_page == 5
    assert second_page.meta.next_cursor is not None
    second_ids = {p.id for p in second_page.data}

    # Verify different players are returned
    assert not first_ids.intersection(second_ids)


def test_get_player_season_stats(client):
    response = client.epl.players.get_season_stats(player_id=PLAYER_ID, season=2024)
    assert len(response.data) > 0
    stat = response.data[0]
    assert stat.value is not None
    assert stat.name is not None
    assert stat.season == 2024


def test_list_epl_games_pagination(client):
    # Test first page
    first_page = client.epl.games.list(season=2024, per_page=5)
    assert len(first_page.data) == 5
    assert first_page.meta.per_page == 5
    assert first_page.meta.next_cursor is not None
    first_ids = {g.id for g in first_page.data}

    # Test second page
    second_page = client.epl.games.list(
        season=2024, per_page=5, cursor=first_page.meta.next_cursor
    )
    assert len(second_page.data) == 5
    assert second_page.meta.per_page == 5
    second_ids = {g.id for g in second_page.data}

    # Verify different games are returned
    assert not first_ids.intersection(second_ids)


def test_get_game_lineups(client):
    response = client.epl.games.get_lineups(game_id=12785)
    assert len(response.data) > 0
    lineup = response.data[0]
    assert lineup.team_id is not None
    assert lineup.player.id is not None


def test_get_game_goals(client):
    response = client.epl.games.get_goals(game_id=12785)
    goal = response.data[0]
    assert goal.game_id == 12785
    assert goal.scorer is not None
    assert goal.clock is not None


def test_get_game_team_stats(client):
    response = client.epl.games.get_team_stats(game_id=12785)
    assert response.data.game_id == 12785
    assert len(response.data.teams) > 0


def test_get_game_player_stats(client):
    response = client.epl.games.get_player_stats(game_id=12785)
    assert response.data.game_id == 12785
    assert len(response.data.players) > 0


def test_get_epl_standings(client):
    response = client.epl.standings.get(season=2024)
    assert len(response.data) > 0
    standing = response.data[0]
    assert standing.team is not None
    assert standing.position > 0
    assert standing.overall_points >= 0


def test_list_player_stat_leaders_pagination(client):
    # Test first page
    first_page = client.epl.leaders.players.list(season=2024, type="goals", per_page=5)
    for player in first_page.data:
        assert player.value is not None
        assert player.name == "goals"
    assert len(first_page.data) == 5
    assert first_page.meta.per_page == 5
    assert first_page.meta.next_cursor is not None
    first_players = {l.player.id for l in first_page.data}

    # Test second page
    second_page = client.epl.leaders.players.list(
        season=2024, type="goals", per_page=5, cursor=first_page.meta.next_cursor
    )
    assert len(second_page.data) == 5
    assert second_page.meta.per_page == 5
    second_players = {l.player.id for l in second_page.data}

    # Verify different players are returned
    assert not first_players.intersection(second_players)

    # Verify order (should be descending by value)
    assert all(
        first_page.data[i].value >= first_page.data[i + 1].value
        for i in range(len(first_page.data) - 1)
    )


def test_list_team_stat_leaders_pagination(client):
    # Test first page
    first_page = client.epl.leaders.teams.list(season=2024, type="goals", per_page=5)
    for team in first_page.data:
        assert team.value is not None
        assert team.name == "goals"
    assert len(first_page.data) == 5
    assert first_page.meta.per_page == 5
    assert first_page.meta.next_cursor is not None
    first_teams = {l.team.id for l in first_page.data}

    # Test second page
    second_page = client.epl.leaders.teams.list(
        season=2024, type="goals", per_page=5, cursor=first_page.meta.next_cursor
    )
    assert len(second_page.data) == 5
    assert second_page.meta.per_page == 5
    second_teams = {l.team.id for l in second_page.data}

    # Verify different teams are returned
    assert not first_teams.intersection(second_teams)

    # Verify order (should be descending by value)
    assert all(
        first_page.data[i].value >= first_page.data[i + 1].value
        for i in range(len(first_page.data) - 1)
    )
