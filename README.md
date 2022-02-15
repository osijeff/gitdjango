# gitdjango
this project is to master every aspect of git and github

CHAPTER ONE: PROJECT SETUP
step # 1  let create virtual enviroment

        syntax: virtualenv gitP

step # 2 activate virtual

         syntax: gitP\Scripts\activate

step # 3 install Django

        syntax: pip install django

step # 4 start django project

         syntax: django-admin startproject tshop

step # 5 create application

         syntax: python manage.py startapp shop


step # 6 register shop application in among the listed app in settings.py

        syntax:  'shop'

step # 7 run the development server

        syntax: python manage.py runserver

HURRAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YOU JUST CREATED YOUR FIRST  APLLICATION

CHAPTER TWO: SET UP THE FRONT-END


step # 1 create a templates folder in the root folder

step # 2 configure the templates in settings.py file

        syntax:     
        
         TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))], # new, 

step # 3 create a file name _base.html in your newely created folder and create HTML boilaplate in there. create title block and content block 
        syntax: <title>{% block title %} Home{% endblock %}</title>

        {% block content %} content{% endblock %}

step # 4 create home.html file in the templates folder and extends the _base.html into home.html file

        syntax: {% extends '_base.html' %}

step # 5 create home view function to handle home template in views.py

        syntax: def HomePageView(request):
                    return render(request, 'home.html')

step # 6 create a urls.py file inside the shop app to list all the shop app view functions. dn't forget to import path and views modules 

        syntax: app_name = 'home'
                urlpatterns=[
                path('', HomePageView, name='home'),
                ]


step # 7 register the shop url inside project urls file. dnt forget to import include module

        syntax: path('', include('shop.urls', namespace='shop')),


WORKING ON NAVIGATION, 
Step # 1 include static folder
step # 2 configure the static folder in settings.py file

        syntax:        STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'),]
                       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

step # 3 load static in base .html
        syntax: {% load static %}

step 4 link css in base.html
        syntax : <link rel="stylesheet" href="{% static 'css/style.css'%}">

step 5 link the bootstrap
        syntax: <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.10.2/mdb.min.js"></script>