import copy
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def isolated_activities():
    """Provide a clean activities state for each test."""
    state = copy.deepcopy(app_module.activities)
    with patch.object(app_module, "activities", state):
        yield state


@pytest.fixture
def client(isolated_activities):
    """Provide a TestClient bound to the app with isolated state."""
    with TestClient(app_module.app) as test_client:
        yield test_client
