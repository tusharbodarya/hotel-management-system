from django.urls import path

from hotel import views

app_name = 'hotel'

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<slug>/", views.hotel_detail, name="hotel-detail"),
    path("detail/<slug:slug>/room-type/<slug:rt_slug>/", views.room_type_detail, name="room-type-detail"),
    path("selected_rooms/", views.selected_rooms, name="selected_rooms"),
    path("checkout/<booking_id>/", views.checkout, name="checkout"),
]
