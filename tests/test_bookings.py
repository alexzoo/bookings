from models.booking_model import (BookingCreateRequest, BookingDates,
                                  BookingCreateResponse, BookingGetByIdResponse)


class TestBookings:

    def test_get_booking_ids(self, bookings):
        data = bookings.get_all()
        assert len(data) > 1

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

    def test_get_booking_by_name(self, bookings):
        data = bookings.get_by_name('Alex', 'Zoo')
        assert len(data) > 0

    def test_get_with_details_by_id(self, bookings):
        booking_id = 1
        response = bookings.get_by_id(booking_id)
        booking_response = BookingGetByIdResponse(**response)
        assert isinstance(booking_response.firstname, str)
        assert isinstance(booking_response.lastname, str)

    def test_cant_delete_booking_by_incorrect_id(self, bookings):
        booking_id = 9999999
        bookings.delete(booking_id, expected_status=405)
