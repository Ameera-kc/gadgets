from django.urls import path

from api.v1.product_api.views import CategoryAPI, ProductAPI

app_name = 'product_api'

urlpatterns = [
    path('category/', CategoryAPI.as_view({'post': 'create'}), name='category-create'),
    path('category/retrieve/<int:pk>/', CategoryAPI.as_view({'get': 'retrieve'}), name='category-retrieve'), 
    path('category/update/<int:pk>/', CategoryAPI.as_view({'put': 'update'}), name='category-update'), 
    path('category/delete/<int:pk>/', CategoryAPI.as_view({'delete': 'destroy'}), name='category-delete'),     
    path('category/list/', CategoryAPI.as_view({'get': 'list'}), name='category-list'),
    
    path('product/', ProductAPI.as_view({'post': 'create'}), name='product-create'),
    path('product/retrieve/<int:pk>/', ProductAPI.as_view({'get': 'retrieve'}), name='product-retrieve'), 
    path('product/update/<int:pk>/', ProductAPI.as_view({'put': 'update'}), name='product-update'), 
    path('product/delete/<int:pk>/', ProductAPI.as_view({'delete': 'destroy'}), name='product-delete'),     
    path('product/list/', ProductAPI.as_view({'get': 'list'}), name='product-list'),
    
]