import pytest


@pytest.mark.smoke
def test_cant_get_booking_by_incorrect_id(bookings):
    booking_id = 9999999
    bookings.get_by_id(booking_id, expected_status=404)
