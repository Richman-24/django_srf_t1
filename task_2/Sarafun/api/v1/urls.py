from django.urls import include, path

from api.v1.users.urls import users_urls
from api.v1.goods.urls import goods_urls

urlpatterns = [
    path('', include(users_urls)),
    path('', include(goods_urls)),
]