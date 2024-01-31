import pytest

from models.booking_model import BookingID, BookingGetByIdResponse


class TestGetBookingsIds:

    @pytest.mark.smoke
    def test_get_all_booking_ids(self, bookings):
        response = bookings.get_all()

        assert len(response) > 1
        for booking_id in response:
            BookingID(**booking_id)

    @pytest.mark.smoke
    def test_get_booking_by_id(self, bookings, create_new_booking):
        booking_id = create_new_booking.bookingid
        firstname = create_new_booking.booking.firstname
        lastname = create_new_booking.booking.lastname
        response = bookings.get_by_id(booking_id=booking_id)

        booking_response = BookingGetByIdResponse(**response)
        assert booking_response.firstname == firstname
        assert booking_response.lastname == lastname

    @pytest.mark.smoke
    def test_get_booking_by_name(self, bookings, create_new_booking):
        booking_id = create_new_booking.bookingid
        firstname = create_new_booking.booking.firstname
        lastname = create_new_booking.booking.lastname
        data = bookings.get_by_name(firstname, lastname)

        assert any(item.get("bookingid") == booking_id for item in data)

    @pytest.mark.smoke
    def test_get_bookings_by_checkin_date(self, bookings, create_new_booking):
        checkin_date = create_new_booking.booking.bookingdates.checkin
        data = bookings.get_by_checkin(checkin_date)

        assert len(data) >= 1

    @pytest.mark.smoke
    def test_get_bookings_by_checkout_date(self, bookings, create_new_booking):
        checkout_date = create_new_booking.booking.bookingdates.checkout
        data = bookings.get_by_checkout(checkout_date)

        assert len(data) >= 1

    @pytest.mark.smoke
    def test_cant_get_booking_by_incorrect_id(self, bookings):
        booking_id = 9999999
        bookings.get_by_id(booking_id, expected_status=404)


