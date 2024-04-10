from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType

@csrf_exempt
def check_room_availability(request):
    if request.method == "POST":
        id = request.POST.get("hotel_id")
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        adult = request.POST.get("adult")
        children = request.POST.get("children")
        room_type = request.POST.get("room_type")
        
        hotel = Hotel.objects.get(id=id)
        room_type = RoomType.objects.get(hotel=hotel, slug=room_type)
        
        url = reverse("hotel:room-type-detail", args=(hotel.slug, room_type.slug))
        url_with_params = f"{url}?hotel_id={id}&checkin={checkin}&checkout={checkout}&adult={adult}&children={children}&room_type={room_type}"
        return HttpResponseRedirect(url_with_params)