from django.urls import path
from . import views

urlpatterns = [

    #base urls
    path('', views.loginPage, name='loginPage'), #this will be the default page
    path('registerPage/', views.registerPage, name='registerPage'), #sign up page
    path('portalPage/', views.portalPage, name='portalPage'), #portal page
    path('new', views.new, name='new'), #new page
    path('login2', views.login2, name='login2'), #login page

    #userReg urls
    path('testPage1/', views.testPage1, name='testPage1'),
    path('registerFreemium/', views.registerFreemium, name='registerFreemium'),
    path('registerTurtle/', views.registerTurtle, name='registerTurtle'),



    
]
