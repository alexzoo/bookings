import pytest
from services.booking_service import Bookings


@pytest.fixture
def bookings():
    return Bookings()
