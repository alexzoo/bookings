from models.booking_model import BookingCreateRequest, BookingDates, BookingCreateResponse, BookingUpdateResponse
import allure


class TestUpdateBooking:

    def test_update_booking(self, bookings):
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

        with allure.step('Update booking'):
            update_booking_data = BookingCreateRequest(firstname='Alexey',
                                                       lastname='Zubec',
                                                       totalprice=555,
                                                       depositpaid=False,
                                                       bookingdates=BookingDates(checkin='2025-02-10',
                                                                                 checkout='2025-02-20'),
                                                       additionalneeds='No Breakfast')
            update_response = bookings.update(booking_id, update_booking_data=update_booking_data.model_dump())

            update_booking_response = BookingUpdateResponse(**update_response)
            assert update_booking_response.firstname == update_booking_data.firstname
            assert update_booking_response.lastname == update_booking_data.lastname
            assert update_booking_response.totalprice == update_booking_data.totalprice
            assert update_booking_response.depositpaid == update_booking_data.depositpaid
            assert update_booking_response.bookingdates.checkin == update_booking_data.bookingdates.checkin
            assert update_booking_response.bookingdates.checkout == update_booking_data.bookingdates.checkout
            assert update_booking_response.additionalneeds == update_booking_data.additionalneeds

    # The following test find 1 bug - it's OK
    def test_cant_update_booking_with_incorrect_data(self, bookings):
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
