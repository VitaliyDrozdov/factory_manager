from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("directory.urls")),
    path("api/token/", views.obtain_auth_token, name="token_auth"),
]
