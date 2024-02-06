from models.auth.auth_response_model import AuthResponse


def test_can_create_token(auth):
    response = auth.create_token()

    AuthResponse(**response)

