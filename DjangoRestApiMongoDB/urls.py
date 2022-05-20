# django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.
# from django.conf.urls import url
  
from django.urls import include, re_path
 
urlpatterns = [
    re_path(r'^', include('users.urls')),
]