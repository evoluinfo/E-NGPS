from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("login.urls")),
    path("app/", include("base.urls")),
    path('admin/', admin.site.urls),
]
