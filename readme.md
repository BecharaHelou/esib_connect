# Esib Connect

### Introduction:
The website goal is to have more exposure to clubs and even create your own club.

### How to run:
First you need to install the dependencies:
```
pip install -r requirements.txt
```

Second you need to migrate:
```
python manage.py migrate
```

Then in order to run the server on local host, run this command:
```
python manage.py runserver
```

Then open your browser and enter this url: http://127.0.0.1:8000/

### Quick tour around the source code:

##### 1)ClubNetwork/
Contain the main application code:  
static/ folder contain mostly css and javascript  
templates/ folder contain all the html files  
models.py file is the logic for the database structure  
urls.py file define all the routes in our website  
views.py file contain the most code and is the center of the application logic  

##### 2)EsibConnect/settings.py
This file contain most of the settings for our project

### How to use the website:
When you open the website you can register as a student or as a club. Then you can start messing around and check your profile and edit it.  
If you registered as a student you can like other club posts and follow them.  
If you registered as a club you can do same as the students but also create posts. But in order to create posts you need to have your club verified (need at least 10 followers). Once you submited a verification request to the admin, you'll have to wait to the admin response.  
You can setup your own admin account.
```
python manage.py createsuperuser
```
After creating your superuser you'll be able to access http://127.0.0.1:8000/admin and then you can head to your user and check the "is admin" checkbox.