import pytest

from services.ping_service.ping_service import Ping


@pytest.fixture
def ping():
    return Ping()
