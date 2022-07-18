import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient

from base.models import Product

client = APIClient()
'''
Integration testing testing api to register user
'''
@pytest.mark.django_db
def test_registration():
    payload = dict(
        name="amar",
        email="test11@test.com",
        password="test123456&"
    )
    response = client.post("/api/users/register/", payload)
    data = response.data
    assert data["name"] == payload["name"]
    assert data["username"] == payload["email"]
    assert "password" not in data

@pytest.mark.django_db
def test_login():
    payload = dict(
        name="amar",
        email="test11@test.com",
        password="test123456&"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", dict(username="test11@test.com",password="test123456&"))
    data = response.data
    assert data["username"] == payload["email"]
    assert "password" not in data
    assert response.status_code == 200


@pytest.mark.django_db
# wrong username and pass
def test_Invalid_Username():
    response = client.post("/api/users/login/", dict(username="amarbb_kk@gmail",password="asasasasa"))
    assert response.status_code == 401 # 401 for failed login

@pytest.mark.django_db
# mandatory fields
def test_mandatory_fields():
    response = client.post("/api/users/login/", dict(username="amarbb_kk@gmail"))
    assert response.status_code == 400 # 400 client error

# def test_profille():
#     payload = dict(
#         name="amar",
#         email="test11@test.com",
#         password="test123456&"
#     )
#     client.post("/api/users/register/", payload)
#     client.post("/api/users/login/", dict(username="test11@test.com", password="test123456&"))
#     response = client.get('/api/users/profile')
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_logout():
#     payload = dict(
#         name="amar",
#         email="test11@test.com",
#         password="test123456&"
#     )
#     client.post("/api/users/register/", payload)
#     client.post("/api/users/login/", dict(username="test11@test.com", password="test123456&"))
#


