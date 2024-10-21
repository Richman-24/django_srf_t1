from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from goods.models import Category, Product
from api.v1.goods.serializers import CategorySerializer, ProductSerializer

User = get_user_model()


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

