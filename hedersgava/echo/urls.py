"""
specifics urls for echo apps
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.echo, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
]
