import pytest

from models.booking_model import BookingID, BookingGetByIdResponse, BookingCreateRequest, BookingCreateResponse, \
    BookingDates


class TestGetBookingsIds:

    @pytest.mark.smoke
    def test_get_all_booking_ids(self, bookings):
        response = bookings.get_all()

        assert len(response) > 1
        for booking_id in response:
            BookingID(**booking_id)

    def test_get_booking_by_id(self, bookings, create_booking):
        booking_id = create_booking.bookingid
        firstname = create_booking.firstname
        lastname = create_booking.lastname
        response = bookings.get_by_id(booking_id=booking_id)

        booking_response = BookingGetByIdResponse(**response)
        assert booking_response.firstname == firstname
        assert booking_response.lastname == lastname

    def test_get_booking_by_name(self, bookings, create_booking):
        firstname = create_booking.firstname
        lastname = create_booking.lastname
        data = bookings.get_by_name(firstname, lastname)

        assert data == ''

    @pytest.mark.smoke
    def test_get_bookings_by_checkin_date(self, bookings):
        data = bookings.get_by_checkin('2023-02-10')

        assert len(data) > 0

    @pytest.mark.smoke
    def test_get_bookings_by_checkout_date(self, bookings):
        data = bookings.get_by_checkout('2023-02-20')

        assert len(data) > 0

    @pytest.mark.smoke
    def test_cant_get_booking_by_incorrect_id(self, bookings):
        booking_id = 9999999
        bookings.get_by_id(booking_id, expected_status=404)


@pytest.fixture(scope='function')
def create_booking(bookings):
    booking_data = BookingCreateRequest(firstname='Alex',
                                        lastname='Zoo',
                                        totalprice=111,
                                        depositpaid=True,
                                        bookingdates=BookingDates(checkin='2024-02-10',
                                                                  checkout='2024-02-20'),
                                        additionalneeds='Breakfast')
    response = bookings.create(booking_data=booking_data.model_dump())
    booking_response = BookingCreateResponse(**response)

    yield booking_response
    bookings.delete(booking_id=booking_data.bookingid)
