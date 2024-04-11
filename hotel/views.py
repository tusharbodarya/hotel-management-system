from django.shortcuts import render, redirect
from django.contrib import messages
from hotel.models import Hotel, Booking, ActivityLog, StaffOnDuty, Room, RoomType
from datetime import datetime
def index(request):
    hotels = Hotel.objects.filter(status="Live")
    context = {
        "hotels": hotels,
    }
    return render(request, 'hotel/index.html', context)

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    context = {
        "hotel": hotel,
    }
    return render(request, 'hotel/hotel_detail.html', context)

def room_type_detail(request, slug, rt_slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)
    
    id = request.GET.get("hotel_id")
    checkin = request.GET.get("checkin")
    checkout = request.GET.get("checkout")
    adult = request.GET.get("adult")
    children = request.GET.get("children")
        
    context = {
        "hotel": hotel,
        "room_type": room_type,
        "rooms": rooms,
        "checkin": checkin,
        "checkout": checkout,
        "adult": adult,
        "children": children,
    }
    return render(request, 'hotel/room_type_detail.html', context)

def selected_rooms(request):
    
    total = 0
    room_count = 0
    total_days = 0
    adult = 0
    children = 0
    checkin = ""
    checkout = ""
    
    if 'selection_data_obj' in request.session:
        
        if request.method == 'POST':
            for h_id, item in request.session["selection_data_obj"].items():
                hotel_id = int(item["hotel_id"])
                room_id = int(item["room_id"])
                room_type_id = int(item["room_type_id"])
                checkin = item["checkin"]
                checkout = item["checkout"]
                adult = int(item["adult"])
                children = int(item["children"])
                
                user = request.user
                hotel = Hotel.objects.get(id=hotel_id)
                room = Room.objects.get(id=room_id)
                room_type = RoomType.objects.get(id=room_type_id)
                
                
            date_format = "%Y-%m-%d"
            checkin_date = datetime.strptime(checkin, date_format)
            checkout_date = datetime.strptime(checkout, date_format)
            time_diffrence = checkout_date - checkin_date
            total_days = time_diffrence.days
        
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            
            booking = Booking.objects.create(
                hotel=hotel,
                room_type=room_type,
                ckeck_in_date=checkin,
                ckeck_out_date=checkout,
                total_days=total_days,
                num_adults=adult,
                num_children=children,
                room=room,
                full_name=full_name,
                email=email,
                phone=phone,
                user=request.user or None,
            )
            
            # if request.user.is_authenticated:
            #     booking.user = request.user
            #     booking.save()
            # else:
            #     booking.user = None
            #     booking.save()

            for h_id, item in request.session["selection_data_obj"].items():
                room_id = int(item['room_id'])
                room = Room.objects.get(id=room_id)
                booking.room.add(room)
                
                room_count += 1
                days = total_days
                price =room_type.price
                
                room_price = price * room_count
                total = room_price * days
            
            booking.total += float(total)
            booking.before_discount += float(total)
            booking.save()
            
            return redirect("hotel:checkout", booking.booking_id)
            
            
        hotel = None
        for h_id, item in request.session["selection_data_obj"].items():
            hotel_id = int(item["hotel_id"])
            room_id = int(item["room_id"])
            room_type_id = int(item["room_type_id"])
            checkin = item["checkin"]
            checkout = item["checkout"]
            adult = int(item["adult"])
            children = int(item["children"])
            
            room_type = RoomType.objects.get(id=room_type_id)
            
            date_format = "%Y-%m-%d"
            checkin_date = datetime.strptime(checkin, date_format)
            checkout_date = datetime.strptime(checkout, date_format)
            time_diffrence = checkout_date - checkin_date
            total_days = time_diffrence.days
            
            room_count += 1
            days = total_days
            price =room_type.price
            
            room_price = price * room_count
            total = room_price * days
            
            hotel = Hotel.objects.get(id=hotel_id)
            
        context = {
            "data": request.session['selection_data_obj'],
            "total_selected_items": len(request.session['selection_data_obj']),
            "total": total,
            "room_count": room_count,
            "adult": adult,
            "children": children,
            "checkin": checkin,
            "checkout": checkout,
            "total_days": total_days,
            "hotel": hotel,
        }
        return render(request, 'hotel/selected_rooms.html', context) 
    else:
        context = {
            "data": {},
            "total_selected_items": 0
        }
        messages.warning(request,"No Selected Rooms Yet...")
        return redirect("/")

def checkout(request, booking_id):
    booking = Booking.objects.get(booking_id=booking_id)
    context = {
        "booking": booking,
    }
    return render(request, 'hotel/checkout.html', context)