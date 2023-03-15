from django.urls import path
from . import views

urlpatterns = [
    path('testPage1/', views.testPage1, name='testPage1'),
    path('registerFreemium/', views.registerFreemium, name='registerFreemium'),
    path('registerTurtle/', views.registerTurtle, name='registerTurtle'),
    path('logout/', views.logoutUser, name='logout'),

    

    
]
