from django.contrib import admin
from .models import Venue, Event, User, Cart
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(User)
admin.site.register(Cart)
