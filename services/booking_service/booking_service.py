from utils.helpers import parse_json_response
import allure


class Bookings:
    # for update and delete methods needs only admin token
    ADMIN_TOKEN_HEADER = {"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="}

    def __init__(self, api_client):
        self.api_client = api_client

    @allure.step("Get all bookings")
    def get_all(self, expected_status=200):
        """
        Send a GET request to '/booking' and assert the response status code is as expected.
        Return the parsed JSON response.
        """
        response = self.api_client.get('/booking')
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Get booking by name')
    def get_by_name(self, firstname, lastname, expected_status=200):
        """
        Sends a GET request to the '/booking' endpoint with the provided first name and last name as parameters.
        Asserts that the response status code matches the expected status code, and returns the parsed JSON response.

        :param firstname: The first name to be used as a query parameter.
        :param lastname: The last name to be used as a query parameter.
        :param expected_status: The expected HTTP status code (default is 200).
        :return: Parsed JSON response from the GET request.
        """
        params = {'firstname': firstname, 'lastname': lastname}
        response = self.api_client.get('/booking', params=params)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Get booking by ID')
    def get_by_id(self, booking_id, expected_status=200):
        """
        Sends a GET request to retrieve a booking by its ID and checks the status code against the expected status.
        :param booking_id: The ID of the booking to retrieve.
        :param expected_status: The expected status code (default is 200).
        :return: The parsed JSON response from the GET request.
        """
        response = self.api_client.get(f'/booking/{booking_id}')
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Get booking by check-in date')
    def get_by_checkin(self, checkin, expected_status=200):
        """
        Sends a GET request to the '/booking' endpoint with the specified check-in date.
        Asserts that the response status code matches the expected status code.
        Returns the parsed JSON response.
        """
        params = {'checkin': checkin}
        response = self.api_client.get('/booking', params=params)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Get booking by check-out date')
    def get_by_checkout(self, checkout, expected_status=200):
        """
        Sends a GET request to the '/booking' endpoint with the provided checkout parameter.

        :param checkout: The checkout parameter for the request.
        :param expected_status: The expected HTTP status code for the response (default is 200).
        :return: Parsed JSON response from the API.
        """
        params = {'checkout': checkout}
        response = self.api_client.get('/booking', params=params)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Create a new booking')
    def create(self, booking_data, expected_status=200):
        """
        Creates a new booking using the provided booking data.

        :param booking_data: The data for the new booking
        :param expected_status: The expected HTTP status code (default is 200)
        :return: The parsed JSON response from the API
        """
        response = self.api_client.post('/booking', json=booking_data)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Update a booking')
    def update(self, booking_id, update_booking_data, expected_status=200):
        """
        Updates a booking with the given booking ID using the provided data.

        Args:
            booking_id (int): The ID of the booking to be updated.
            update_booking_data (dict): The data to update the booking with.
            expected_status (int, optional): The expected status code of the response. Defaults to 200.

        Returns:
            dict: The JSON response from the API after updating the booking.
        """
        response = self.api_client.put(f'/booking/{booking_id}', json=update_booking_data,
                                       headers=self.ADMIN_TOKEN_HEADER)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)

    @allure.step('Delete a booking by ID')
    def delete(self, booking_id, expected_status=200):
        """
        Delete a booking by its ID.

        :param booking_id: The ID of the booking to be deleted.
        :param expected_status: The expected status code of the response (default is 200).
        :return: The parsed JSON response from the API.
        """
        response = self.api_client.delete(f'/booking/{booking_id}', headers=self.ADMIN_TOKEN_HEADER)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)
