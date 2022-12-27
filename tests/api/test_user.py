import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        email = "dilshadkhan@gmail.com",
        username = "dilshad",
        password = "Test1234@",
        confirm_password = "Test1234@"
    )

    response = client.post("/accounts/signup/",payload)

    data = response.data
   
    assert data["email"] == payload["email"]
    assert data["username"] == payload["username"]
    assert "password" not in data
  

@pytest.mark.django_db
def test_login(user, client):

    response = client.post("/accounts/login/",dict(email="dilshad@gmail.com",password="Test1234@"))
    
    assert response.status_code == 200
    data = response.data
    
    assert "token" in data


@pytest.mark.django_db
def test_login_failed(client):
    response = client.post("/accounts/login/",dict(email="dilshad@gmail.com",password="Test124@"))

    assert response.status_code == 400


@pytest.mark.django_db
def test_primeNumber(user, authClient):
    
    response = authClient.post("/prime/",dict(min=1,max=10))

    assert response.status_code == 200

    data = response.data
    assert "primeNumber" in data

