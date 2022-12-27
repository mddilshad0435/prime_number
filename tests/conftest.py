import pytest
from rest_framework.test import APIClient
from accounts.models import User

@pytest.fixture
def user():
    # user_data = {
    #     "email":"dilshad@gmail.com",
    #     "username":"dilshad",
    #     "password":"Test1234@"
    # }
    user = User.objects.create_user(email="dilshad@gmail.com",username="dilshad",password="Test1234@")
    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def authClient(user,client):
    client.post("/accounts/login/",dict(email="dilshad@gmail.com",password="Test1234@"))
    token = user.get_tokens_for_user()
    token = token['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
