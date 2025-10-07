from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking

# Serializers define the API representation.
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'duration']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'booking_status']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id', 'username']

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'seat', 'user', 'booking_date']
        read_only_fields = ['booking_date']

class BookingCreateSerializer(serializers.Serializer):
    """Serializer for creating a new booking"""
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())

    def validate_seat(self, value):
        """Ensure seat is available"""
        if value.booking_status:
            raise serializers.ValidationError("This seat is already booked")
        return value