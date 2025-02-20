from django.contrib import admin
from .models import Vehicle, Booking, Payment, Review, LoyaltyProgram

admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(LoyaltyProgram)