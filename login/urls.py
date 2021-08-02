from django.views.generic import TemplateView
from django.urls import path
from login import views


urlpatterns = [
    path('', views.logar_usuario, name="login"),
    path('app/deslogar_usuario', views.deslogar_usuario, name="deslogar_usuario"),
    path('cadastrar_usuario', views.cadastrar_usuario, name="cadastrar_usuario"),
]