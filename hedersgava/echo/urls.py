"""
specifics urls for echo apps
"""
from django.urls import path
from . import views

urlpatterns = [# pylint: disable=invalid-name
    path('data/', views.echo, name='data store'),
    path('data/<int:filter_timestamp>/', views.echo_filter, name='detail'),
]
