
from models.booking_model import BookingRequest, BookingDates, BookingResponse


class TestBookings:

    def test_get_booking_ids(self, bookings):
        data = bookings.get_all()
        assert len(data) > 1

    def test_create_booking(self, bookings):
        booking_data = BookingRequest(firstname='Alex',
                                      lastname='Zoo',
                                      totalprice=111,
                                      depositpaid=True,
                                      bookingdates=BookingDates(checkin='2024-02-10',
                                                                checkout='2024-02-20'),
                                                                additionalneeds='Breakfast')

        response = bookings.create(booking_data=booking_data.model_dump())
        booking_response = BookingResponse(**response)
        assert booking_response.booking == booking_data

    def test_get_booking_by_name(self, bookings):
        data = bookings.get_by_name('Alex', 'Zoo')
        assert len(data) > 0

    def test_get_with_details_by_id(self, bookings):
        booking_id = 1770
        data = bookings.get_by_id(booking_id)
        assert 'Alex' in data['firstname']
        assert 'Zoo' in data['lastname']

    def test_cant_delete_booking_by_incorrect_id(self, bookings):
        booking_id = 9999999
        bookings.delete(booking_id, expected_status=405)
