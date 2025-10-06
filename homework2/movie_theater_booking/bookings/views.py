from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Movie, Seat, Booking
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer, BookingCreateSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the bookings index.")

class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['get'])
    def available_seats(self, request, pk=None):
        movie = self.get_object()
        available_seats = Seat.objects.filter(booking_status=False)
        serializer = SeatSerializer(available_seats, many=True)
        return Response({
            'movie': movie.title,
            'available_seats': serializer.data
        })

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def get_queryset(self):
        """
        Filter seats by availability
        """
        queryset = Seat.objects.all()
        available = self.request.query_params.get('available')
        
        if available:
            is_available = available.lower() in ['true', '1', 'yes']
            queryset = queryset.filter(booking_status=not is_available)
        
        return queryset

    @action(detail=False, methods=['get'])
    def available(self, request):
        """
        Get all available seats
        GET /seats/available/
        """
        available_seats = Seat.objects.filter(booking_status=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def booked(self, request):
        """
        Get all booked seats
        GET /seats/booked/
        """
        booked_seats = Seat.objects.filter(booking_status=True)
        serializer = self.get_serializer(booked_seats, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for users to book seats and view their booking history.
    
    Provides:
    - list: GET /bookings/ (user's bookings)
    - create: POST /bookings/
    - retrieve: GET /bookings/{id}/
    - update: PUT /bookings/{id}/
    - partial_update: PATCH /bookings/{id}/
    - destroy: DELETE /bookings/{id}/
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return bookings for the current user only
        Admin users can see all bookings
        """
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def get_serializer_class(self):
        """
        Use different serializers for create vs list/retrieve
        """
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new booking and mark seat as booked
        POST /bookings/
        Expected payload: {
            "movie": 1,
            "seat": 1
        }
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        movie = serializer.validated_data['movie']
        seat = serializer.validated_data['seat']
        
        # Check if seat is available
        if seat.booking_status:
            return Response(
                {'error': 'This seat is already booked'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create booking
        with transaction.atomic():
            booking = Booking.objects.create(
                user=request.user,
                movie=movie,
                seat=seat
            )
            
            # Mark seat as booked
            seat.booking_status = True
            seat.save()
        
        return Response(
            BookingSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['get'])
    def my_bookings(self, request):
        """
        Get current user's booking history
        GET /bookings/my_bookings/
        """
        bookings = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """
        Cancel a booking and free up the seat
        POST /bookings/{id}/cancel/
        """
        booking = self.get_object()
        
        # Check if user owns this booking
        if booking.user != request.user and not request.user.is_staff:
            return Response(
                {'error': 'You can only cancel your own bookings'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Free the seat and delete booking
        with transaction.atomic():
            seat = booking.seat
            seat.booking_status = False
            seat.save()
            booking.delete()
        
        return Response({
            'message': 'Booking cancelled successfully'
        })

    @action(detail=False, methods=['get'])
    def by_movie(self, request):
        """
        Get bookings filtered by movie
        GET /bookings/by_movie/?movie_id=1
        """
        movie_id = request.query_params.get('movie_id')
        
        if not movie_id:
            return Response(
                {'error': 'movie_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        bookings = self.get_queryset().filter(movie_id=movie_id)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)
