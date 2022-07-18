from rest_framework.response import Response
import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from base.models import Review

from base.models import Product

client = APIClient()

@pytest.mark.django_db
def test_api_product_creation():
    client = APIClient()
    user = User.objects.create_user(username='test1',password='123567',is_staff=True)
    client.force_authenticate(user)
    response = client.post("/api/products/create/")
    data = response.data
    assert data["name"] == " Product Name "
    assert data["brand"] == "Sample brand "
    assert data["countInStock"] == 0
    assert data["category"] == "Sample category"
    assert data["description"] == " "