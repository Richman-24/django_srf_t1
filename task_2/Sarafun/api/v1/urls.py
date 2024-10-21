from django.urls import include, path

from api.v1.users.urls import users_urls

urlpatterns = [
    path('', include(users_urls)),
]