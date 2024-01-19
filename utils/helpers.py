import json
from requests import Response


def parse_json_response(response: Response) -> dict:
    """Converts a JSON response from an API into a Python dictionary.
        Args:
            response: Response object from the requests library.
        Returns:
            A dictionary representing the JSON response.
        Raises:
            ValueError: If the response is not valid JSON.
        """
    try:
        return response.json()
    except json.JSONDecodeError:
        raise ValueError("Response is not a valid JSON")