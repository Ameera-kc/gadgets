from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from api.v1.product_api.serializers import CategorySerializer, ProductListSerializer, ProductSerializer
from product.models import Category, Product


class CategoryAPI(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by('-id')
    
    @swagger_auto_schema(operation_description='List all active categorys')
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)    
    
    @swagger_auto_schema(operation_description='Retrieve category details by ID')
    def retrieve(self, request, pk=None):
        contract = get_object_or_404(Category, id=pk, is_deleted=False)
        serializer = CategorySerializer(contract)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CategorySerializer, operation_description='Create a new category')
    def create(self, request):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():  
            serializer.save()
            return Response({"message": "category created successfully"}, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(request_body=CategorySerializer, operation_description='Update category details')
    def update(self, request, pk=None):
        invoice = get_object_or_404(Category, id=pk, is_deleted=False)
        serializer = CategorySerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(candidate=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)    

    @swagger_auto_schema(operation_description='Deactivate category')
    def destroy(self, request, pk=None):
        invoice = get_object_or_404(Category, id=pk, is_deleted=False)
        invoice.active = False
        invoice.save()
        return Response({"message": "category deactivated successfully"}, status=200)


class ProductAPI(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('-id')
    
    @swagger_auto_schema(operation_description='List all active Products')
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)    
    
    @swagger_auto_schema(operation_description='Retrieve Product details by ID')
    def retrieve(self, request, pk=None):
        contract = get_object_or_404(Product, id=pk, is_deleted=False)
        serializer = ProductSerializer(contract)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer, operation_description='Create a new Product')
    def create(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():  
            serializer.save()
            return Response({"message": "Product created successfully"}, status=201)
        return Response(serializer.errors, status=400)

    @swagger_auto_schema(request_body=ProductSerializer, operation_description='Update Product details')
    def update(self, request, pk=None):
        invoice = get_object_or_404(Product, id=pk, is_deleted=False)
        serializer = ProductSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(candidate=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)    

    @swagger_auto_schema(operation_description='Deactivate Product')
    def destroy(self, request, pk=None):
        invoice = get_object_or_404(Product, id=pk, is_deleted=False)
        invoice.active = False
        invoice.save()
        return Response({"message": "Product deactivated successfully"}, status=200)


