from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path("app/", include("base.urls")),
    path('admin/', admin.site.urls),
]
