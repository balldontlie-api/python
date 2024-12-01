# BALLDONTLIE API

Official Python SDK for the BALLDONTLIE API. Access NBA, NFL, and MLB statistics and data. Check out the official website [here](https://app.balldontlie.io).

## Installation

```bash
# Install the latest version
pip install balldontlie

# Install a specific version
pip install balldontlie==0.1.0
```

## Usage

```python
from balldontlie import BalldontlieAPI

api = BalldontlieAPI(api_key="your-api-key")

# NBA (see documentation for full list of methods)
api.nba.teams.list()

# MLB
api.mlb.teams.list()

# NFL
api.nfl.teams.list()

```

## API Reference

Check out the full API documentation:
[NBA](https://nba.balldontlie.io)
[NFL](https://nfl.balldontlie.io)
[MLB](https://mlb.balldontlie.io)

## Error Handling

```python
from balldontlie import BalldontlieAPI
from balldontlie.exceptions import (
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError,
    BallDontLieException
)

client = BalldontlieAPI(api_key="your_key")

try:
    teams = client.nba.teams.list()
except AuthenticationError as e:
    print(f"Invalid API key. Status: {e.status_code}, Details: {e.response_data}")
except RateLimitError as e:
    print(f"Rate limit exceeded. Status: {e.status_code}, Details: {e.response_data}")
except ValidationError as e:
    print(f"Invalid request parameters. Status: {e.status_code}, Details: {e.response_data}")
except NotFoundError as e:
    print(f"Resource not found. Status: {e.status_code}, Details: {e.response_data}")
except ServerError as e:
    print(f"API server error. Status: {e.status_code}, Details: {e.response_data}")
except BallDontLieException as e:
    print(f"General API error. Status: {e.status_code}, Details: {e.response_data}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
```
