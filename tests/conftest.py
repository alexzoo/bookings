import pytest

from utils.api_client import ApiClient
from services.booking_service import Bookings


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def bookings(api_client):
    return Bookings(api_client)
