import pytest


@pytest.mark.smoke
def test_cant_delete_nonexistent_booking(bookings):
    booking_id = 9999999
    bookings.delete(booking_id, expected_status=405)
