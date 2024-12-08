from product.models import Category, Product
from api.v1.product_api.serializers import CategorySerializer, ProductSerializer
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile


# Test CategorySerializer
@pytest.mark.django_db
def test_category_serializer():
    # Create a category instance
    category = Category(name="Fashion")
    serializer = CategorySerializer(category)
    # Check serialized data
    assert serializer.data == {"name": "Fashion"}

# Test ProductSerializer
@pytest.mark.django_db
def test_product_serializer():
    # Create a category instance
    category = Category.objects.create(name="Electronics")
     # Create a fake image file
    image_content = SimpleUploadedFile(
        name='test_image.jpg',
        content=b'file_content',  # Simulate image content; real image data would be bytes of an actual image.
        content_type='image/jpeg'
    )
    # Open the actual image file in binary mode
    # with open('tests/images/test_image.jpg', 'rb') as image:
    #     image_content = image.read()
    # Create a product instance
    product = Product.objects.create(
        name="Django for APIs",
        price=500,
        category=category,
        description="Learn APIs with Django.",
        image=image_content
    )
    serializer = ProductSerializer(product)
    # Check serialized data
    assert serializer.data['name'] == "Django for APIs"
    assert serializer.data['price'] == 500
    assert serializer.data['category'] == category.id
