from django.test.testcases import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
]
