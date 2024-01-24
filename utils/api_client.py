import json
from typing import Any
from urllib.parse import urlparse, parse_qs

import requests
from requests import Response, Session
from dotenv import load_dotenv
import os
import logging


# load .env
load_dotenv()
log_level = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self) -> None:
        self.base_url: str = os.getenv('API_BASE_URL')
        self.token: str = os.getenv('TOKEN')
        self.session: Session = requests.Session()
        if self.token:
            self.session.headers.update({"Authorization": f"Basic {self.token}"})
        self.logger = logging.getLogger(__name__)

    def log_request(self, response: Response) -> None:
        self.logger.info(f"Request URL: {response.request.url}")
        self.logger.info(f"Request Method: {response.request.method}")

        # Log the request headers
        headers = response.request.headers
        formatted_headers = json.dumps(dict(headers), indent=4)
        self.logger.info(f"Request Headers: {formatted_headers}")

        # Parse the query parameters from the URL
        parsed_url = urlparse(response.request.url)
        query_params = parse_qs(parsed_url.query)
        if query_params:
            formatted_params = json.dumps(query_params, indent=4)
            self.logger.info(f"Request Params: {formatted_params}")

        if response.request.body:
            self.logger.info(f"Request Body: {response.request.body}")

    def log_response(self, response: Response) -> None:
        self.logger.info(f"Response Status Code: {response.status_code}")

        # Log the response headers
        headers = response.headers
        formatted_headers = json.dumps(dict(headers), indent=4)
        self.logger.info(f"Response Headers: {formatted_headers}")

        self.logger.info(f"Response Body: {response.text}")

    def get(self, path: str, **kwargs: Any) -> Response:
        response = self.session.get(url=f'{self.base_url}{path}', **kwargs)
        self.log_request(response)
        self.log_response(response)
        return response

    def post(self, path: str, data: dict = None, json: dict = None, **kwargs: Any) -> Response:
        response = self.session.post(url=f"{self.base_url}{path}", data=data, json=json, **kwargs)
        self.log_request(response)
        self.log_response(response)
        return response

    def put(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        response = self.session.put(url=f"{self.base_url}{path}", data=data, **kwargs)
        self.log_request(response)
        self.log_response(response)
        return response

    def delete(self, path: str, **kwargs: Any) -> Response:
        response = self.session.delete(url=f"{self.base_url}{path}", **kwargs)
        self.log_request(response)
        self.log_response(response)
        return response

    def patch(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        response = self.session.patch(url=f"{self.base_url}{path}", data=data, **kwargs)
        self.log_request(response)
        self.log_response(response)
        return response
