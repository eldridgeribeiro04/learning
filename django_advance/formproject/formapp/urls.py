from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form_name_view, name='form')
]