import os
import pytest
import warnings
import urllib3
from balldontlie import BalldontlieAPI

warnings.filterwarnings("ignore", category=urllib3.exceptions.NotOpenSSLWarning)

@pytest.fixture
def api_key():
    return os.environ.get("BALLDONTLIE_API_KEY", "test_key")

@pytest.fixture
def client(api_key):
    return BalldontlieAPI(api_key=api_key)