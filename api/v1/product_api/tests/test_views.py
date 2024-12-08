import pytest
from rest_framework.test import APIClient
from product.models import Category, Product
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
import os
# Set up APIClient for making requests
client = APIClient()

# Test Category List View
@pytest.mark.django_db
def test_category_list_view():
    # Create categories
    Category.objects.create(name="Electronics")
    Category.objects.create(name="Furnitures")
    # Make a GET request to the category list endpoint
    response = client.get('/api/v1/category/list/')
    # Check the response
    assert response.status_code == 200
    assert len(response.data) == 2
    # assert response.data[0]['name'] == "Electronics"

@pytest.mark.django_db
def test_category_create_view():
    # Make a POST request to create a category
    response = client.post('/api/v1/category/', {"name": "Fashion"})
    
    # Debugging: Print the response data in case of error
    print(response.data)  # This will help in debugging the response
    
    # Check the response
    assert response.status_code == 201
    assert response.data["message"] == "category created successfully"


# Test Product Create View
@pytest.mark.django_db
def test_product_create_view():
    # Create a category first
    category = Category.objects.create(name="Electronics")
    assert category.id is not None  # Ensure category is created
    
    # Create a fake image file
    # image_content = SimpleUploadedFile(
    #     name='test_image.jpg',
    #     content=b'file_content',  # Simulate image content; real image data would be bytes of an actual image.
    #     content_type='image/jpeg'
    # )

    # with open('tests/images/test_image.jpg', 'rb') as image:
    #     image_content = image.read()

    image_path = os.path.join(os.path.dirname(__file__), 'images', 'test_image.jpg')
    with open(image_path, 'rb') as image_file:
        image_content = SimpleUploadedFile(
            name='test_image.jpg',
            content=image_file.read(),
            content_type='image/jpeg'
        )
    # Make a POST request to create a product
    response = client.post('/api/v1/product/', {
        "name": "Django for Beginners",
        "price": 500,
        "category": category.id,
        "description": "A beginner-friendly Django book.",
        "image": image_content  # Include the image field
    })
    
    # Check the response
    print(response.data) 
    print("vfyebdsiazgvhcnjxvchjx")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == "Product created successfully"
    
    # Ensure the product is created in the database (optional, but good practice)
    # product = Product.objects.get(name="Django for Beginners")
    # assert product.name == "Django for Beginners"
    # assert product.price == 500
    # assert product.category == category
    # assert product.description == "A beginner-friendly Django book."
    # assert product.image.name.endswith('test_image.jpg')  # Check the image name (optional)
