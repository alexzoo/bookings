import json
import logging
import os
from urllib.parse import urlparse, parse_qs

from dotenv import load_dotenv

load_dotenv()
log_level = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=log_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ApiLogger:
    def __init__(self, name=__name__):
        self.logger = logging.getLogger(name)

    @staticmethod
    def format_headers(headers):
        return json.dumps(dict(headers), indent=4, sort_keys=True)

    @staticmethod
    def format_body(body):
        try:
            return json.dumps(json.loads(body), indent=4, sort_keys=True)
        except (TypeError, json.JSONDecodeError):
            return body

    @staticmethod
    def format_params(params):
        return json.dumps(parse_qs(urlparse(params).query), indent=4, sort_keys=True)

    def log_request(self, response):
        self.logger.info(f"Request URL: {response.request.url}")
        self.logger.info(f"Request Method: {response.request.method}")
        self.logger.info(f"Request Headers: {self.format_headers(response.request.headers)}")

        if response.request.body:
            self.logger.info(f"Request Body: {self.format_body(response.request.body)}")

        parsed_url = urlparse(response.request.url)
        if parsed_url.query:
            self.logger.info(f"Request Params: {self.format_params(response.request.url)}")

    def log_response(self, response):
        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Headers: {self.format_headers(response.headers)}")
        self.logger.info(f"Response Body: {self.format_body(response.text)}")
