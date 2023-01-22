# meetdrf
Place to learn Django Rest Framework

## Step by Step
A. Django Preparation
1. Install django framework package (in terminal)
2. Start django project (in terminal django-admin startproject project_name.)
3. Setup django project
* create_app(in terminal manage.py startapp app_name)
* install app (in project_name/settings.py INSTALLED APPS) into project
* create html file tamplate (in app_name/template_name.html)
* setup template DIRS path (in project_name/settings.py TEMPLATES)
* add static path (in project_name/settings.py STATIC_URL), static files(css, js, etc.)
* add media path (in project_name/settings.py MEDIA_URL), media files

4. Setup django app
* create urls.py (in app_name/)
* include desired urls (app_name/urls) for the app (in project_name/urls.py urlpattern)
* create views function or classes (in app_name/views.py)
* open route from url to views function (in app_name/urls.py)

B. Web Scraper Preparation
* Install Selenium (in terminal)
* Create 
