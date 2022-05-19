# django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+.
# from django.conf.urls import url
  
from django.urls import include, re_path
from users import views 
 
urlpatterns = [ 
    re_path(r'^api/users$', views.user_list),
    re_path(r'^api/users/(?P<pk>[0-9]+)$', views.user_detail),
    re_path(r'^api/users/published$', views.user_list_published)
]