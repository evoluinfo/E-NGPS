from django.urls import path
from client import views


urlpatterns = [
    path('client/', views.client, name='client'),
    path('form_client/', views.form_client, name='form_client'),
    path('create_client/', views.create_client, name='create_client'),
    path('view_client/<int:pk>', views.view_client, name='view_client'),
    path('edit_client/<int:pk>/', views.edit_client, name='edit_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
    path('delete_client/<int:pk>', views.delete_client, name='delete_client'),
]