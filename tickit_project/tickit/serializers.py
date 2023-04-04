from rest_framework import serializers
from .models import Venue, User, Event


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True,
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue',
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'venue_id', 'artist', 'date', 'time',
                  'description', 'price', 'ticket_count', 'category', 'all_ages')


# class CartSerializer(serializers.HyperlinkedModelSerializer):
#     user = serializers.HyperlinkedRelatedField(
#         view_name='user_detail',
#         read_only=True,
#     )
#     events = serializers.HyperlinkedRelatedField(
#         view_name='event_detail',
#         many=True,
#         read_only=True,
#     )

#     user_id = serializers.PrimaryKeyRelatedField(
#         queryset=User.objects.all(),
#         source='user',
#     )

#     event_id = serializers.PrimaryKeyRelatedField(
#         queryset=Event.objects.all(),
#         source='events',
#     )

#     class Meta:
#         model = Cart
#         fields = ('id', 'user_id', 'event_id', 'user', 'events')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True,
    )

    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail',
    )

    class Meta:
        model = User
        fields = ('id', 'user_url', 'username', 'email', 'password', 'events')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True,
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail',
    )

    class Meta:
        model = Venue
        fields = ('id', 'venue_url', 'name', 'address', 'phone',
                  'capacity', 'accessible', 'parking', 'hours', 'events')
