from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path("api/", include("directory.urls")),
    path("api/token/", views.obtain_auth_token, name="token_auth"),
]
