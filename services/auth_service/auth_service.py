from client.api_client import ApiClient
from utils.helpers import parse_json_response
import allure


class Auth:
    def __init__(self):
        self.api_client = ApiClient()

    @allure.step("Create a token using the provided username and password")
    def create_token(self, username='admin', password='password123', expected_status=200):
        """
        Creates a token using the provided username and password.

        :param username: The username for authentication (default: 'admin')
        :param password: The password for authentication (default: 'password123')
        :param expected_status: The expected HTTP status code (default: 200)
        :return: The parsed JSON response
        """
        data = {
            'username': username,
            'password': password
        }

        response = self.api_client.post('/auth', data=data)
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return parse_json_response(response)
