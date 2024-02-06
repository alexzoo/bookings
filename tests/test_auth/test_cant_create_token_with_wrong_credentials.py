import pytest
from faker import Faker


@pytest.mark.smoke
def test_cant_create_token_with_wrong_credentials(auth, create_user_and_password):
    username, password = create_user_and_password
    token = auth.create_token(username=username, password=password)
    assert token['reason'] == 'Bad credentials'


@pytest.fixture
def create_user_and_password():
    faker = Faker()
    username = faker.user_name()
    password = faker.password()
    return username, password
