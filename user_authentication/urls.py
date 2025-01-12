from . import views
from django.urls import path

app_name = 'authentication'  # This defines the namespace

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]