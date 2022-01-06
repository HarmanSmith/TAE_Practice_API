import pytest
import json


@pytest.fixture
def config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config
