from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField()
    capacity = models.IntegerField()
    accessible = models.BooleanField()
    parking = models.CharField()
    hours = models.CharField()

    def __str__(self):
        return self.name
    

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.user
    

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='events')
    artist = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField()
    price = models.IntegerField()
    ticket_count = models.IntegerField()
    category = models.CharField(max_length=100)
    all_ages = models.BooleanField()

    def __str__(self):
        return self.artist


    

