from django.shortcuts import render, get_object_or_404

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html')

def ContactPageView(request):
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
    return render(request, 'pages/contact.html')

def CatogoriesPageView(request):
    return render(request,'pages/categories.html')    
=======
=======
>>>>>>> upstream/main
>>>>>>> fa13979283c4d98dd86a94c7d09cfd2e68243bea
    return render(request, 'pages/contact.html') 


def CartPageView(request):
<<<<<<< HEAD
    return render(request, 'pages/cart.html')      
=======
<<<<<<< HEAD
    return render(request, 'pages/cart.html')      
>>>>>>> upstream/main
=======
    return render(request, 'pages/cart.html')      
>>>>>>> upstream/main
>>>>>>> fa13979283c4d98dd86a94c7d09cfd2e68243bea
