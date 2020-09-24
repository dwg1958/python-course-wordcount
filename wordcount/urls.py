"""wordcount URL Configuration"""
from django.contrib import admin
from django.urls import path

# NB: import the page templates
from . import views, views2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('david/', views.david),
    path('count/', views2.count, name="count"),
    path('', views.home),
]
