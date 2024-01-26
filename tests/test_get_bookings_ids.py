from models.booking_model import BookingID, BookingGetByIdResponse


class TestGetBookingsIds:

    def test_get_all_booking_ids(self, bookings):
        response = bookings.get_all()

        assert len(response) > 1
        for booking_id in response:
            BookingID(**booking_id)

    def test_get_booking_by_id(self, bookings):
        booking_id = 3
        response = bookings.get_by_id(booking_id=booking_id)

        booking_response = BookingGetByIdResponse(**response)
        assert isinstance(booking_response.firstname, str)
        assert isinstance(booking_response.lastname, str)

    def test_get_booking_by_name(self, bookings):
        data = bookings.get_by_name('Alex', 'Zoo')

        assert len(data) > 0

    def test_get_bookings_by_checkin_date(self, bookings):
        data = bookings.get_by_checkin('2023-02-10')

        assert len(data) > 0

    def test_get_bookings_by_checkout_date(self, bookings):
        data = bookings.get_by_checkout('2023-02-20')

        assert len(data) > 0

    def test_cant_get_booking_by_incorrect_id(self, bookings):
        booking_id = 9999999
        bookings.get_by_id(booking_id, expected_status=404)
