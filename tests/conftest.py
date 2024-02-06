import pytest

from client.api_client import ApiClient
from services.auth_service.auth_service import Auth


@pytest.fixture(scope="session")
def auth_token():
    auth = Auth()
    token_response = auth.create_token()
    token = token_response['token']
    return token


@pytest.fixture(scope="session")
def api_client(auth_token):
    client = ApiClient()
    client.session.headers.update({"Authorization": f"Basic {auth_token}"})
    return client
