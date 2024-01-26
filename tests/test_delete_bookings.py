import allure

from models.booking_model import BookingCreateRequest, BookingDates, BookingCreateResponse


class TestDeleteBookings:

    def test_delete_booking_by_id(self, bookings):
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

        with allure.step('Delete booking'):
            bookings.delete(booking_id, expected_status=201)

        with allure.step('Try to get deleted booking'):
            bookings.get_by_id(booking_id, expected_status=404)

        with allure.step('Try to delete deleted booking'):
            bookings.delete(booking_id, expected_status=405)