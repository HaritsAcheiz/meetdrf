from django.urls import path
from dsapp import views

urlpatterns = [
    path("", views.ds, name="ds" )
]