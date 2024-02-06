from utils.api_client import ApiClient


class Ping:
    def __init__(self):
        self.api_client = ApiClient()

    def health_check(self, expected_status=201):
        """
        Perform a health check by sending a GET request to '/ping' endpoint and asserting the response status code
        against the expected status code.

        Args:
            self: The object instance
            expected_status (int): The expected status code (default is 200)

        Returns:
            response: The response object from the GET request
        """
        response = self.api_client.get('/ping')
        assert response.status_code == expected_status, (f"Unexpected status code: {response.status_code}, "
                                                         f"expected: {expected_status}")
        return response
