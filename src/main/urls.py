from django.urls import path, include

api_version = '/v1/'

urlpatterns = [
    path(f"api{api_version}", include("api.urls")),
]
