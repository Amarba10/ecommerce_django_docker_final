import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient

from base.models import Product

client = APIClient()
'''
Unit tests -> checking user creation func
'''
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('amar','barake@gmail.com','barake123456')
    count = User.objects.all().count()
    assert count == 1

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("test2345")
    assert user_1.check_password("test2345") is True

@pytest.mark.django_db
def test_update_username(user_1):
    user=User.objects.create_user('test2','amarbava@gmail.com','amaro')
    user_update=User.objects.get(id=user_1.id)
    user_update.username='barake'
    assert 'barake' == user_update.username

