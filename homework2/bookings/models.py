from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_number}"

class Booking(models.Model):
    movie = models.CharField(max_length=200)
    seat = models.IntegerField()
    user = models.CharField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seat {self.seat.seat_number}"