"""
specifics urls for echo apps
"""
from django.urls import path
from . import views

urlpatterns = [# pylint: disable=invalid-name
    path('', views.echo, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
]
