from utils.helpers import parse_json_response


class Bookings:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_all(self, expected_status=200):
        """
        Sends a GET request to retrieve all bookings from the API.

        :param expected_status: The expected HTTP status code (default is 200).
        :type expected_status: int
        :return: Parsed JSON response from the API.
        :rtype: dict
        :raises ValueError: If the response status code is not the expected status code.
        """
        response = self.api_client.get('/booking')
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def get_by_name(self, firstname, lastname, expected_status=200):
        """
        Sends a GET request to retrieve a booking by first and last name.

        Args:
            firstname (str): The first name of the booking.
            lastname (str): The last name of the booking.
            expected_status (int, optional): The expected status code of the response. Defaults to 200.

        Raises:
            ValueError: If the response status code is not the expected status code.

        Returns:
            dict: The parsed JSON response from the API.
        """
        params = {'firstname': firstname, 'lastname': lastname}
        response = self.api_client.get('/booking', params=params)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def get_by_id(self, booking_id, expected_status=200):
        """
        Sends a GET request to retrieve booking information by ID.

        Args:
            booking_id (int): The ID of the booking to retrieve.
            expected_status (int, optional): The expected HTTP status code. Defaults to 200.

        Returns:
            dict: The parsed JSON response containing the booking information.

        Raises:
            ValueError: If the response status code does not match the expected status.
        """
        response = self.api_client.get(f'/booking/{booking_id}')
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def create(self, booking_data, expected_status=200):
        """
        Makes a POST request to create a booking with the provided data.

        Args:
            booking_data: The data for creating the booking.
            expected_status: The expected HTTP status code (default is 200).

        Returns:
            The parsed JSON response from the POST request.
        """
        response = self.api_client.post('/booking', json=booking_data)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)

    def delete(self, booking_id, expected_status=200):
        """
        Deletes a booking by sending a DELETE request to the API.

        Args:
            booking_id (int): The ID of the booking to be deleted.
            expected_status (int, optional): The expected status code of the response. Defaults to 200.

        Returns:
            dict: The parsed JSON response from the API.

        Raises:
            ValueError: If the response status code is not the expected status code.
        """
        response = self.api_client.delete(f'/booking/{booking_id}')
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}, expected: {expected_status}")
        return parse_json_response(response)