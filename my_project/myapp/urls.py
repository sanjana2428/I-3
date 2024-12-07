from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage
    path('loginpage/', views.loginpage, name='loginpage'),  # Login page
    path('register/', views.register, name='register'),  # Register page
]
