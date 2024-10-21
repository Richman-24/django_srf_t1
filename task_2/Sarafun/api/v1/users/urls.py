from django.urls import include, path

users_urls = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]