import pytest


@pytest.mark.smoke
def test_get_bookings_by_checkout_date(bookings, create_new_booking):
    checkout_date = create_new_booking.booking.bookingdates.checkout
    data = bookings.get_by_checkout(checkout_date)

    assert len(data) >= 1

