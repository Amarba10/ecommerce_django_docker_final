
import pytest
# @pytest.mark.django_db
# def test_product_created():
#   Product.objects.create
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from base.models import Review

from base.models import Product

#unit test- testing if prpduct can be created as a unit (by it self with out dependecies)
def create_product():
  return Product.objects.create(
        name=" Product Name ",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" ")

def create_product_review():
    return Review.objects.create(
        product=create_product(),
        name=User.username,
        rating=3,
        comment="good enough")

@pytest.mark.django_db
def test_product_creation():
    p = create_product()
    assert isinstance(p, Product) is True
    assert p.name == " Product Name "

@pytest.mark.django_db
def test_ProductReview():
    p = create_product_review()
    assert p.rating == 3
    assert p.comment == "good enough"





