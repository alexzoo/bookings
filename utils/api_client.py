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
        self.token: str = os.getenv('TOKEN')
        self.session: Session = requests.Session()
        if self.token:
            self.session.headers.update({"Authorization": f"Basic {self.token}"})
        self.logger = ApiLogger(__name__)

    def get(self, path: str, **kwargs: Any) -> Response:
        response = self.session.get(url=f'{self.base_url}{path}', **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def post(self, path: str, data: dict = None, json: dict = None, **kwargs: Any) -> Response:
        response = self.session.post(url=f"{self.base_url}{path}", data=data, json=json, **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def put(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        response = self.session.put(url=f"{self.base_url}{path}", data=data, **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def delete(self, path: str, **kwargs: Any) -> Response:
        response = self.session.delete(url=f"{self.base_url}{path}", **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response

    def patch(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        response = self.session.patch(url=f"{self.base_url}{path}", data=data, **kwargs)
        self.logger.log_request(response)
        self.logger.log_response(response)
        return response
