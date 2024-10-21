from django.urls import path
from api.v1.goods.views import CategoryListView

goods_urls = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
]