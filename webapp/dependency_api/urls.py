from django.urls import path
from dependency_api import views

urlpatterns = [
    path('', views.home_page),
    path('api/dependency_parse', views.parse_dependency),
]