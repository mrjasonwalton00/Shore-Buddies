from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landingScreen/', include('landingScreen.urls')),
    path('', include('userReg.urls')),
]
