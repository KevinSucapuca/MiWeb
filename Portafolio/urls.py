
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
urlpatterns = [
    path('adminportafolio/', admin.site.urls),
    path('', include('portafolios.urls')),
]


handler404 = 'portafolios.views.custom_404'
