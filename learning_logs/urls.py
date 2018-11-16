"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

    # SHow all topics.
    path('topics/', views.topics, name='topics'),
]
