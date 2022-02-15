from unicodedata import name
from .views import *
from django.urls import path

app_name = 'home'
urlpatterns=[
path('', HomePageView, name='home'),
path('contact', ContactPageView, name = 'contact'),
<<<<<<< HEAD
path('categories',CatogoriesPageView ,name= 'categories')
=======
path('cart', CartPageView, name = 'cart'),
>>>>>>> upstream/main
]