from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup_doc', views.signup_doc, name='signup_doc'),
    path('signup_patient', views.signup_patient, name='signup_patient'),
]