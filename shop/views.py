from django.shortcuts import render, get_object_or_404

# Create your views here.
def HomePageView(request):
    return render(request, 'home.html')

def ContactPageView(request):
    return render(request, 'pages/contact.html')

def SubscibePageView(request):
    return render(request,'pages/subscribe.html' )  