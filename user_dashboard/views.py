from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType, HotelGallery, Coupon, Notification

@login_required
def dashboard(request):
    booking = Booking.objects.filter(user=request.user, payment_status="Paid")
    total_spent = Booking.objects.filter(user=request.user, payment_status="Paid").aggregate(amount=models.Sum("total"))
    
    context = {
        "booking": booking,
        "total_spent": total_spent,
    }
    
    return render(request, "user_dashboard/dashboard.html", context)

@login_required
def booking_detail(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id, user=request.user, payment_status="Paid")
    
    context = {
        "booking": booking,
    }
    
    return render(request, "user_dashboard/booking_detail.html", context)