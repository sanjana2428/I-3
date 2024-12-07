from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('patient/', views.patient_dashboard, name='patient_dashboard'),
    path('provider/', views.provider_dashboard, name='provider_dashboard'),
    path('logout/', views.logout_view, name='logout'),

]
