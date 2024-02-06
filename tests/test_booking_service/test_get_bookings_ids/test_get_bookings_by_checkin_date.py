import pytest


@pytest.mark.with_errors
def test_get_bookings_by_checkin_date(bookings, create_new_booking):
    checkin_date = create_new_booking.booking.bookingdates.checkin
    data = bookings.get_by_checkin(checkin_date)

    assert len(data) >= 1
