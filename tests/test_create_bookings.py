import pytest

from models.booking_create_response_model import BookingCreateResponse
from models.booking_create_request_model import BookingCreateRequest
from models.booking_dates_model import BookingDates


class TestCreateBookings:

    @pytest.mark.smoke
    def test_create_booking(self, bookings):
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

    # The following tests find 4 bugs - it's OK
    @pytest.mark.with_error
    @pytest.mark.parametrize(
        "firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds, expected_status", [
            ('', 'Zoo', 111, True, '2024-02-10', '2024-02-20', 'Breakfast', 400),  # Empty firstname
            ('Alex', '', 111, True, '2024-02-10', '2024-02-20', 'Breakfast', 400),  # Empty lastname
            ('Alex', 'Zoo', -100, True, '2024-02-10', '2024-02-20', 'Breakfast', 400),  # Negative totalprice
            ('Alex', 'Zoo', 111, True, '2024-02-20', '2024-02-10', 'Breakfast', 400),  # Invalid dates order
        ],
        ids=[
            'empty_firstname',
            'empty_lastname',
            'negative_totalprice',
            'invalid_dates_order'
        ]
    )
    def test_cant_create_booking_with_incorrect_data(self, bookings, firstname, lastname, totalprice, depositpaid,
                                                     checkin, checkout, additionalneeds, expected_status):
        booking_data = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }

        bookings.create(booking_data, expected_status=expected_status)
