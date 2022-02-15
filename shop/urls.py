from .views import *
from django.urls import path

app_name = 'home'
urlpatterns=[
path('', HomePageView, name='home'),
path('contact', ContactPageView, name = 'contact'),
path('cart', CartPageView, name = 'cart'),
]