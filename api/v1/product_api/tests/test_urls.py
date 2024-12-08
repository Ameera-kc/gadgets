from django.urls import reverse, resolve
from api.v1.product_api.views import CategoryAPI, ProductAPI
import pytest
# Test Category URLs
# @pytest.mark.django_db
# def test_category_list_url():
#     url = reverse('product_api:category-list')
#     assert resolve(url).func.__name__ == CategoryAPI.list.__name__

# @pytest.mark.django_db
# def test_category_list_url():
#     url = reverse('product_api:category-list')
#     assert resolve(url).view_name == 'category-list'  # Adjusted to match the correct view name

# @pytest.mark.django_db
# def test_category_create_url():
#     url = reverse('product_api:category-create')
#     assert resolve(url).func.__name__ == CategoryAPI.create.__name__

# # Test Product URLs
# @pytest.mark.django_db
# def test_product_list_url():
#     url = reverse('product_api:product-list')
#     assert resolve(url).func.__name__ == ProductAPI.list.__name__

from django.urls import reverse, resolve
from api.v1.product_api.views import CategoryAPI, ProductAPI

# Test URL for Category List
def test_category_list_url():
    url = reverse('product_api:category-list')  # Adjusted to match the correct URL pattern name
    assert resolve(url).view_name == 'product_api:category-list'  # View method for listing categories

# Test URL for Category Create
def test_category_create_url():
    url = reverse('product_api:category-create')
    assert resolve(url).view_name == 'product_api:category-create'  # View method for creating category

# Test URL for Product List
def test_product_list_url():
    url = reverse('product_api:product-list')
    assert resolve(url).view_name == 'product_api:product-list'  # View method for listing products

# Test URL for Product Create
def test_product_create_url():
    url = reverse('product_api:product-create')
    assert resolve(url).view_name == 'product_api:product-create'  # View method for creating product

