from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('allproduct/', allproduct, name='allproduct'),
    path('product/<slug:title>/', product, name='product'),
    path('services/', services, name='services'),
    path('industries/', industries, name='industries'),
    path('quality/', quality, name='quality'),
    path('career/', career, name='career'),
    path('contact/', contect, name='contact'),
    

]