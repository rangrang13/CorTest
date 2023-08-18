import rest_framework
from django.urls import path, include, re_path
from . import views

app_name = 'notion_app'
urlpatterns = [
    path('', include('rest_framework.urls', namespace = 'rest_framework_category'))
]
