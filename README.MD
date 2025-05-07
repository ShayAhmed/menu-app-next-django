# To install and setup
 - py -m venv venv
 - .\venv\Scripts\activate
 - pip install django djangorestframework
 - django-admin startproject RestaurantCore .

settings.py - contains all config of project
urls.py - all urls of the project
wsgi - usefil for running project in development mode and also for deployment

menu/models.py - contains representation of table in db
menu/serializers.py - converts JSON to python native object
menu/viewsets.py - defines controller that handles requests
./routers.py - contains all endpoints for api, will need to register in urls.py
ResturantCore/urls.py - register router here