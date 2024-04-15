from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType, HotelGallery, Coupon, Notification
from django.contrib import messages

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


@login_required
def bookings(request):
    bookings = Booking.objects.filter(user=request.user, payment_status="Paid")
    
    context = {
        "bookings": bookings,
    }
    
    return render(request, "user_dashboard/bookings.html", context)
    
@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, seen=False)
    
    context = {
        "notifications": notifications,
    }
    
    return render(request, "user_dashboard/notifications.html", context)

def notification_mark_as_seen(request, id):
    notifications = Notification.objects.get(id=id)
    notifications.seen = True
    notifications.save()
    messages.success(request, "Notification seen")
    return redirect("user_dashboard:notifications")


@login_required
def wallet(request):
    booking = Booking.objects.filter(user=request.user, payment_status="Paid")
    total_spent = Booking.objects.filter(user=request.user, payment_status="Paid").aggregate(amount=models.Sum("total"))
    wallet_balance = request.user.profile.wallet
    context = {
        "booking": booking,
        "total_spent": total_spent,
        "wallet_balance": wallet_balance,
    }
    
    return render(request, "user_dashboard/wallet.html", context)