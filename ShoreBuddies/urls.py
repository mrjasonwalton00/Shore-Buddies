from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('userReg/', include('userReg.urls')), #this is the path to the userReg app

  
   
]
