import pytest
import json

from client.client import ReqResClient


@pytest.fixture
def config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


@pytest.fixture
def reqres_client(config) -> ReqResClient:
    """Obtains a new API client for ReqRes service"""
    yield ReqResClient(config['url'])
