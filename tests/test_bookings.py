class TestBookings:

    def test_get_booking_ids(self, bookings):
        data = bookings.get_all()
        assert len(data) > 1

    def test_create_booking(self, bookings):

        json_data = {
            'firstname': 'Alex',
            'lastname': 'Zoo',
            'totalprice': 111,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2024-02-01',
                'checkout': '2024-02-10'
            },
            'additionalneeds': 'Breakfast'
        }

        data = bookings.create(json_data)
        assert data['booking'] == json_data

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
        # bookings.get_by_id(booking_id, expected_status=404)
        bookings.delete(booking_id, expected_status=405)
