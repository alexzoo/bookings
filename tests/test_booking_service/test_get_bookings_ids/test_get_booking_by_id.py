import pytest

from models.booking.booking_get_by_id_response_model import BookingGetByIdResponse


@pytest.mark.smoke
def test_get_booking_by_id(bookings, create_new_booking):
    booking_id = create_new_booking.bookingid
    firstname = create_new_booking.booking.firstname
    lastname = create_new_booking.booking.lastname
    response = bookings.get_by_id(booking_id=booking_id)

    booking_response = BookingGetByIdResponse(**response)
    assert booking_response.firstname == firstname
    assert booking_response.lastname == lastname

