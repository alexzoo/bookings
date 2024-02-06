import allure
import pytest

from models.booking.booking_create_request_model import BookingCreateRequest
from models.booking.booking_create_response_model import BookingCreateResponse
from models.booking.booking_dates_model import BookingDates


# The following test find 1 bug - it's OK
@pytest.mark.with_errors
def test_cant_update_booking_with_incorrect_data(bookings):
    with allure.step('Create new booking'):
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
        # get booking id
        booking_id = booking_response.bookingid

    with allure.step('Update booking with incorrect data'):
        update_booking_data = {'firstname': 'Alexey',
                               'lastname': 'Zubec',
                               'totalprice': 'test',
                               'depositpaid': 'test',
                               'bookingdates': {'checkin': 'test',
                                                'checkout': 'test'},
                               'additionalneeds': 'No Breakfast'}
        bookings.update(booking_id, update_booking_data=update_booking_data, expected_status=400)
