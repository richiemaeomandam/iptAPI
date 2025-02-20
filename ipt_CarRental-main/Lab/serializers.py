from rest_framework import serializers
from .models import Vehicle, Booking, Payment, Review, LoyaltyProgram

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class LoyaltyProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = '__all__'



