# swagger-django-crud
**Product Management Crud API using Django**
This project is a Product Management API built using Django and Django REST Framework. It provides an interface for managing products and their categories, along with an integrated Swagger-based API documentation.

**Features**
- Category Management:
Add, update, retrieve, list, and deactivate categories.

- Product Management:
Add, update, retrieve, list, and deactivate products associated with categories.

- RESTful API Endpoints:
Built-in endpoints for product and category CRUD operations.

- API Documentation:
Interactive Swagger and ReDoc documentation for easy exploration of API endpoints.

**Getting Started**
- Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework
- Pillow (for handling image uploads)
- Installation
- Clone the repository

```
git clone <repository_url>
cd swagger_django_crud
```
- Install dependencies

```
pip install -r requirements.txt
```
- Run database migrations

```
python manage.py migrate
```
- Run the development server

```
python manage.py runserver
```
**Access the API documentation:**

- Swagger UI: http://127.0.0.1:8000/
- ReDoc: http://127.0.0.1:8000/redoc/
