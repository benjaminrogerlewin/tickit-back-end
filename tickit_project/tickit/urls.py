from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('venues', views.venue_list, name='venue_list'),
    path('events', views.event_list, name='event_list')
]