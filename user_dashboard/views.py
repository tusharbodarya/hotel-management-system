from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType, HotelGallery, Coupon, Notification, Bookmark, Review
from userauths.models import Profile
from django.contrib import messages
from django.http import JsonResponse
from userauths.forms import UserUpdateForm, ProfileUpdateFrom
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

@login_required
def bookmark(request):
    bookmark = Bookmark.objects.filter(user=request.user)
    context = {
        "bookmark": bookmark,
    }
    
    return render(request, "user_dashboard/bookmark.html", context)

def delete_bookmark(request, bid):
    bookmark = Bookmark.objects.get(bid=bid)
    bookmark.delete()
    messages.success(request, "Bookmark deleted")
    return redirect("user_dashboard:bookmark")

def add_to_bookmark(request):
    id = request.GET.get("id")
    hotel = Hotel.objects.get(id=id)
    if request.user.is_authenticated:
        bookmark = Bookmark.objects.filter(user=request.user, hotel=hotel)
        if bookmark.exists():
            bookmark = Bookmark.objects.filter(user=request.user, hotel=hotel)
            bookmark.delete()
            return JsonResponse({"data": "Bookmark Deleted", "icon": "success"})
        else:
            Bookmark.objects.create(
                user=request.user,
                hotel=hotel
            )
            return JsonResponse({"data": "Hotel Bookmarked", "icon": "success"})
    else:
        return JsonResponse({"data": "Please Login To Bookmark Hotel", "icon": "warning"})
    
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated")
            return redirect("user_dashboard:profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)
    context = {
        'profile': profile,
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, "user_dashboard/profile.html", context)

@login_required
def password_changed(request):
    return render(request, "user_dashboard/password-reset/password-changed.html")

def add_review(request):
    id = request.GET['id']
    review = request.GET['review']
    rating = request.GET['rating']
    
    hotel = Hotel.objects.get(id=id)
    
    review_check = Review.objects.filter(user=request.user, hotel=hotel)
    if review_check.exists():
        return JsonResponse({"data": "You have already reviewed this hotel", "icon": "warning"})
    else:
        Review.objects.create(
            user=request.user,
            hotel=hotel,
            review=review,
            rating=rating
        )
        return JsonResponse({"data": "Review added", "icon": "success"})