import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import Response, Session

from utils.log_helpers import ApiLogger

# load .env
load_dotenv()


class ApiClient:
    def __init__(self) -> None:
        self.base_url: str = os.getenv('API_BASE_URL')
        self.session: Session = requests.Session()
        self.logger = ApiLogger(__name__)

    def set_token(self, token: str) -> None:
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get(self, path: str, **kwargs: Any) -> Response:
        """
        Send a GET request to the specified path and return the response.

        Args:
            path (str): The path to send the GET request to.
            **kwargs: Additional keyword arguments to pass to the request.

        Returns:
            Response: The response object from the GET request.
        """
        response = self.session.get(url=f'{self.base_url}{path}', **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def post(self, path: str, data: dict = None, json: dict = None, **kwargs: Any) -> Response:
        """
        Sends a POST request to the specified path with optional data and JSON payload.

        Args:
            path (str): The path to send the POST request to.
            data (dict, optional): The data to send in the body of the request.
            json (dict, optional): The JSON payload to send in the body of the request.
            **kwargs: Additional keyword arguments to be passed to the request.

        Returns:
            Response: The response object from the POST request.
        """
        response = self.session.post(url=f"{self.base_url}{path}", data=data, json=json, **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def put(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        """
        Sends a PUT request to the specified path with optional data and additional keyword arguments.

        :param path: The path to send the PUT request to.
        :param data: Optional data to send with the PUT request.
        :param kwargs: Additional keyword arguments to be passed to the underlying requests library.
        :return: The response object from the PUT request.
        """
        response = self.session.put(url=f"{self.base_url}{path}", data=data, **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def delete(self, path: str, **kwargs: Any) -> Response:
        """
        Sends a DELETE request to the specified path and returns the response.

        Args:
            path (str): The path for the DELETE request.
            **kwargs (Any): Additional keyword arguments to be passed to the request.

        Returns:
            Response: The response object from the DELETE request.
        """
        response = self.session.delete(url=f"{self.base_url}{path}", **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def patch(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        """
        Send a PATCH request to the specified path with optional data and return the response.

        :param path: The path for the request
        :type path: str
        :param data: Optional data for the request
        :type data: dict
        :param kwargs: Additional keyword arguments for the request
        :type kwargs: Any
        :return: The response from the PATCH request
        :rtype: Response
        """
        response = self.session.patch(url=f"{self.base_url}{path}", data=data, **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response
