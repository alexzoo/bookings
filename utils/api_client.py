from typing import Any, Dict, Optional

import requests
from requests import Response, Session
from dotenv import load_dotenv
import os


# load .env
load_dotenv()


class ApiClient:
    def __init__(self):
        self.base_url: str = os.getenv('API_BASE_URL')
        self.session: Session = requests.Session()

    def get(self, path: str, **kwargs: Any) -> Response:
        return self.session.get(url=f'{self.base_url}{path}', **kwargs)

    def post(self, path: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs: Any) -> Response:
        return self.session.post(url=f"{self.base_url}{path}", data=data, json=json, **kwargs)

    def put(self, path: str, data: Optional[Dict] = None, **kwargs: Any) -> Response:
        return self.session.put(url=f"{self.base_url}{path}", data=data, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Response:
        return self.session.delete(url=f"{self.base_url}{path}", **kwargs)