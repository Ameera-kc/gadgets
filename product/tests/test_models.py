import pytest
from product.models import Category, Product
from django.core.files.uploadedfile import SimpleUploadedFile

# Test case for Category creation
@pytest.mark.django_db
def test_category_creation():
    # Create a category instance
    category = Category.objects.create(name="Electronics")
    # Assertions to check the created object
    assert category.name == "Electronics"
    assert not category.is_deleted  # Default value is False

# Test case for Product creation
@pytest.mark.django_db
def test_product_creation():
    # Create a category first (Product requires a Category)
    category = Category.objects.create(name="Electronics")
    # Create a fake image file
    image_content = SimpleUploadedFile(
        name='test_image.jpg',
        content=b'file_content',  # Simulate image content; real image data would be bytes of an actual image.
        content_type='image/jpeg'
    )
    # with open('tests/images/test_image.jpg', 'rb') as image:
    #     image_content = image.read()
    # Create a product instance
    product = Product.objects.create(
        name="Django for Beginners",
        price=1000,
        category=category,
        description="A guide to Django.",
        image=image_content
    )
    # Assertions to check the created object
    assert product.name == "Django for Beginners"
    assert product.price == 1000
    assert product.category.name == "Electronics"  # Check relationship
    assert product.is_deleted is False  # Default value
