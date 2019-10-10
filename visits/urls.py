from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('appointment', views.appointment, name='appointment'),
    path('', views.all, name='all'),
    path('<int:visit_id>/', views.detail, name='detail'),
    path('therapy', views.therapy, name='therapy'),
]