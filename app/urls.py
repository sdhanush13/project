from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.Homepage.as_view(),name="home"),
]