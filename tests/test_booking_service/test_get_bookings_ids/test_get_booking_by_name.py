import pytest


@pytest.mark.smoke
def test_get_booking_by_name(bookings, create_new_booking):
    booking_id = create_new_booking.bookingid
    firstname = create_new_booking.booking.firstname
    lastname = create_new_booking.booking.lastname
    data = bookings.get_by_name(firstname, lastname)

    assert any(item.get("bookingid") == booking_id for item in data)
