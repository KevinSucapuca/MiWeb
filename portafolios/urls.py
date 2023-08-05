from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contacto/', views.contact_form, name='contact_form'),
]
