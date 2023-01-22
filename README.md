# meetdrf
Place to learn Django Rest Framework

Step by Step
A. Django Preparation
1. Install django framework package (in terminal)
2. Start django project (in terminal django-admin startproject project_name.)
3. Setup django project
   a. create_app(in terminal manage.py startapp app_name)
   b. install app (in project_name/settings.py INSTALLED APPS) into project
   c. create html file tamplate (in app_name/template_name.html)
   d. setup template DIRS path (in project_name/settings.py TEMPLATES)
   e. add static path (in project_name/settings.py STATIC_URL), static files(css, js, etc.)
   f. add media path (in project_name/settings.py MEDIA_URL), media files
4. Setup django app
   a. create urls.py (in app_name/)
   b. include desired urls (app_name/urls) for the app (in project_name/urls.py urlpattern)
   c. create views function or classes (in app_name/views.py)
   d. open route from url to views function (in app_name/urls.py)

B. Web Scraper Preparation
1. Install Selenium (in terminal)
2. Create 