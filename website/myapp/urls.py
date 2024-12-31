#เลขาห้อง myapp

from django.urls import path
from .views import Homepage, About, Stock, Contact, Service

urlpatterns = [
    path('',Homepage, name='home' ), # localhost:8000 /www.com
    path('about', About, name='about'),
    path('stock', Stock, name='stock'),
    path('contact', Contact, name='contact'),
    path('service', Service, name='service'),
]
