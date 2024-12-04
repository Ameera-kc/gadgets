from django.urls import path

from api.v1.product_api.views import CategoryAPI, ProductAPI

app_name = 'product_api'

urlpatterns = [
    path('category/', CategoryAPI.as_view({'post': 'create'}), name='consultant-invoice-create'),
    path('category/retrieve/<int:pk>/', CategoryAPI.as_view({'get': 'retrieve'}), name='consultant-invoice-retrieve'), 
    path('category/update/<int:pk>/', CategoryAPI.as_view({'put': 'update'}), name='consultant-invoice-update'), 
    path('category/delete/<int:pk>/', CategoryAPI.as_view({'delete': 'destroy'}), name='consultant-invoice-delete'),     
    path('category/list/', CategoryAPI.as_view({'get': 'list'}), name='consultant-invoice-list'),
    
    path('product/', ProductAPI.as_view({'post': 'create'}), name='consultant-invoice-create'),
    path('product/retrieve/<int:pk>/', ProductAPI.as_view({'get': 'retrieve'}), name='consultant-invoice-retrieve'), 
    path('product/update/<int:pk>/', ProductAPI.as_view({'put': 'update'}), name='consultant-invoice-update'), 
    path('product/delete/<int:pk>/', ProductAPI.as_view({'delete': 'destroy'}), name='consultant-invoice-delete'),     
    path('product/list/', ProductAPI.as_view({'get': 'list'}), name='consultant-invoice-list'),
    
]