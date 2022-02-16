from unicodedata import name
from .views import *
from django.urls import path

app_name = 'shop'
urlpatterns=[
path('', HomePageView, name='home'),
<<<<<<< HEAD

=======
path('contact', ContactPageView, name = 'contact'),
<<<<<<< HEAD
<<<<<<< HEAD
path('categories',CatogoriesPageView ,name= 'categories')
=======
path('cart', CartPageView, name = 'cart'),
>>>>>>> upstream/main
=======
path('cart', CartPageView, name = 'cart'),
>>>>>>> upstream/main
>>>>>>> fa13979283c4d98dd86a94c7d09cfd2e68243bea
]