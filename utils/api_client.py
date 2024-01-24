from typing import Any

import requests
from requests import Response, Session
from dotenv import load_dotenv
import os


# load .env
load_dotenv()


class ApiClient:
    def __init__(self) -> None:
        self.base_url: str = os.getenv('API_BASE_URL')
        self.token: str = os.getenv('TOKEN')
        self.session: Session = requests.Session()
        if self.token:
            self.session.headers.update({"Authorization": f"Basic {self.token}"})

    def get(self, path: str, **kwargs: Any) -> Response:
        return self.session.get(url=f'{self.base_url}{path}', **kwargs)

    def post(self, path: str, data: dict = None, json: dict = None, **kwargs: Any) -> Response:
        return self.session.post(url=f"{self.base_url}{path}", data=data, json=json, **kwargs)

    def put(self, path: str, data: dict = None, **kwargs: Any) -> Response:
        return self.session.put(url=f"{self.base_url}{path}", data=data, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Response:
        return self.session.delete(url=f"{self.base_url}{path}", **kwargs)