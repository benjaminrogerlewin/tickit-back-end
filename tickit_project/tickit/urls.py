from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('venues', views.VenueList.as_view(), name='venue_list'),
    path('users', views.UserList.as_view(), name='user_list'),
    path('carts', views.CartList.as_view(), name='cart_list'),
    path('events', views.EventList.as_view(), name='event_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue_detail'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('carts/<int:pk>', views.CartDetail.as_view(), name='cart_detail'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
]
