import pytest

from services.auth_service.auth_service import Auth


@pytest.fixture
def auth():
    return Auth()
