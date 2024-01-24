from utils.helpers import parse_json_response


class Bookings:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_all(self):
        response = self.api_client.get('/booking')
        return parse_json_response(response)

    def get_by_name(self, firstname, lastname):
        params = {'firstname': firstname, 'lastname': lastname}
        response = self.api_client.get('/booking', params=params)
        return parse_json_response(response)

    def get_by_id(self, booking_id):
        response = self.api_client.get(f'/booking/{booking_id}')
        return parse_json_response(response)

    def create(self, booking_data):
        response = self.api_client.post('/booking', json=booking_data)
        return parse_json_response(response)
