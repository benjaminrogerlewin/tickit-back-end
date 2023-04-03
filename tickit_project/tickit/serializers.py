from rest_framework import serializers
from .models import Venue, User, Cart, Event


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'phone',
                  'capacity', 'accessible', 'parking', 'hours', 'events')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True,
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'artist', 'date', 'time',
                  'description', 'price', 'ticket_count', 'category', 'all_ages')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cart = serializers.HyperlinkedRelatedField(
        view_name='cart_detail',
        many=False,
        read_only=True,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'cart')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True,
    )
    events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Cart
        fields = ('id', 'user', 'events')
