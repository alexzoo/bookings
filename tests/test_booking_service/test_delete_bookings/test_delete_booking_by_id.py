import allure
import pytest


@pytest.mark.smoke
def test_delete_booking_by_id(bookings, create_new_booking):

    with allure.step('Create new booking'):
        booking_id = create_new_booking.bookingid

    with allure.step('Delete booking'):
        bookings.delete(booking_id, expected_status=201)

    with allure.step('Try to get deleted booking'):
        bookings.get_by_id(booking_id, expected_status=404)
