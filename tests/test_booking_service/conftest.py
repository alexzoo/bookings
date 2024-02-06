from datetime import timedelta

import allure
import pytest
from faker import Faker

from models.booking.booking_create_response_model import BookingCreateResponse
from models.booking.booking_create_request_model import BookingCreateRequest
from models.booking.booking_dates_model import BookingDates
from services.booking_service.booking_service import Bookings


@pytest.fixture
def bookings():
    return Bookings()


@pytest.fixture(scope='function')
def create_new_booking(bookings):
    with allure.step('Generate fake data'):
        fake = Faker()

        firstname = fake.first_name()
        lastname = fake.last_name()
        totalprice = fake.random_int(min=100, max=1000)
        depositpaid = fake.boolean()
        checkin_date = fake.date_between(start_date="+1y", end_date="+2y")
        checkout_date = checkin_date + timedelta(days=fake.random_int(min=1, max=14))
        additionalneeds = fake.random_element(elements=("Breakfast", "Parking", "WiFi", "Late Checkout"))

    with allure.step('Create new booking'):
        booking_data = BookingCreateRequest(firstname=firstname,
                                            lastname=lastname,
                                            totalprice=totalprice,
                                            depositpaid=depositpaid,
                                            bookingdates=BookingDates(checkin=checkin_date.strftime("%Y-%m-%d"),
                                                                      checkout=checkout_date.strftime("%Y-%m-%d")),
                                            additionalneeds=additionalneeds)
        response = bookings.create(booking_data=booking_data.model_dump())
        booking_response = BookingCreateResponse(**response)

    yield booking_response

    with allure.step('Check if booking exists before deletion'):
        try:
            bookings.get_by_id(booking_id=booking_response.bookingid, expected_status=200)
        except AssertionError as e:
            if "Unexpected status code: 404" in str(e):
                allure.step('Booking not found, skipping deletion')
                return
            else:
                raise

    with allure.step('Delete booking'):
        bookings.delete(booking_id=booking_response.bookingid, expected_status=201)
