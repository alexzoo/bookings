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
        """
        Format the given headers into a JSON string with indentation and sorted keys.

        :param headers: The headers to be formatted into a JSON string.
        :type headers: dict
        :return: A JSON string representation of the formatted headers.
        :rtype: str
        """
        return json.dumps(dict(headers), indent=4, sort_keys=True)

    @staticmethod
    def format_body(body):
        """
        Static method to format the given body using JSON.dumps and JSON.loads.

        Args:
            body: The body to be formatted.

        Returns:
            The formatted body as a JSON string, or the original body if formatting fails.
        """
        try:
            return json.dumps(json.loads(body), indent=4, sort_keys=True)
        except (TypeError, json.JSONDecodeError):
            return body

    @staticmethod
    def format_params(params):
        """
        Format the given parameters as a JSON string with indentation and sorted keys.

        :param params: The parameters to format
        :type params: str

        :return: A JSON string representing the parsed parameters with indentation and sorted keys
        :rtype: str
        """
        return json.dumps(parse_qs(urlparse(params).query), indent=4, sort_keys=True)

    def log_request(self, response):
        """
        Logs the details of the request including URL, method, headers, body, and parameters.

        Args:
            self: The object instance.
            response: The response object containing the request details.

        Returns:
            None
        """
        self.logger.info(f"Request URL: {response.request.url}")
        self.logger.info(f"Request Method: {response.request.method}")
        self.logger.info(f"Request Headers: {self.format_headers(response.request.headers)}")

        if response.request.body:
            self.logger.info(f"Request Body: {self.format_body(response.request.body)}")

        parsed_url = urlparse(response.request.url)
        if parsed_url.query:
            self.logger.info(f"Request Params: {self.format_params(response.request.url)}")

    def log_response(self, response):
        """
        Logs the response status code, headers, and body using the provided response object.

        Args:
            self: The object instance.
            response: The response object received from the API call.

        Returns:
            None
        """
        self.logger.info(f"Response Status Code: {response.status_code}")
        self.logger.info(f"Response Headers: {self.format_headers(response.headers)}")
        self.logger.info(f"Response Body: {self.format_body(response.text)}")
