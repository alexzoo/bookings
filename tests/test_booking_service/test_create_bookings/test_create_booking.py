import pytest

from models.booking.booking_create_request_model import BookingCreateRequest
from models.booking.booking_create_response_model import BookingCreateResponse
from models.booking.booking_dates_model import BookingDates


@pytest.mark.smoke
def test_create_booking(bookings):
    booking_data = BookingCreateRequest(firstname='Alex',
                                        lastname='Zoo',
                                        totalprice=111,
                                        depositpaid=True,
                                        bookingdates=BookingDates(checkin='2024-02-10',
                                                                  checkout='2024-02-20'),
                                        additionalneeds='Breakfast')

    response = bookings.create(booking_data=booking_data.model_dump())

    booking_response = BookingCreateResponse(**response)
    assert booking_response.booking == booking_data

