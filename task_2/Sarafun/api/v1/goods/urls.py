from django.urls import path
from api.v1.goods.views import CategoryListView, ProductDetailView, ProductListView

goods_urls = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]