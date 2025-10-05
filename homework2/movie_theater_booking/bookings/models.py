from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.CharField()

class Booking(models.Model):
    movie = models.CharField(max_length=200)
    seat = models.IntegerField()
    user = models.CharField()
    booking_date = models.DateField()