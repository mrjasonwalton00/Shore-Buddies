from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('registerPage/', views.registerPage, name='registerPage'),
]
