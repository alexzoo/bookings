import pytest

from models.booking.booking_id_model import BookingID


@pytest.mark.smoke
def test_get_all_booking_ids(bookings):
    response = bookings.get_all()

    assert len(response) > 1
    for booking_id in response:
        BookingID(**booking_id)
