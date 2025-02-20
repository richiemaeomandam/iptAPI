from django.shortcuts import render
from rest_framework import generic
from .models import Vehicle, Booking, Payment, Review, LoyaltyProgram
from .serializers import VehicleSerializers, BookingSerializers, PaymentSerializers, ReviewSerializers, LoyaltyProgramSerializers

# Create your views here.
class LabCreateAPIView(generics.ListCreateAPIView):
    queryset = Lab.objects.all()
    serializer_class = PostSerializer

class LabRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lab.objects.all()
    serializer_class = PostSerializer
