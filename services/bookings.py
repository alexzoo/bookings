from utils.helpers import parse_json_response


class Bookings:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_all(self, expected_status=200):
        response = self.api_client.get('/booking')
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def get_by_name(self, firstname, lastname, expected_status=200):
        params = {'firstname': firstname, 'lastname': lastname}
        response = self.api_client.get('/booking', params=params)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def get_by_id(self, booking_id, expected_status=200):
        response = self.api_client.get(f'/booking/{booking_id}')
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def create(self, booking_data, expected_status=200):
        response = self.api_client.post('/booking', json=booking_data)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def delete(self, booking_id, expected_status=200):
        response = self.api_client.delete(f'/booking/{booking_id}')
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)