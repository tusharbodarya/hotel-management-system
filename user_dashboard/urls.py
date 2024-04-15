from django.urls import path
from user_dashboard import views


app_name = "user_dashboard"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("booking-detail/<booking_id>/", views.booking_detail, name="booking_detail"),
    path("bookings/", views.bookings, name="bookings"),
    path("notifications/", views.notifications, name="notifications"),
    path("notification_mark_as_seen/<id>/", views.notification_mark_as_seen, name="notification_mark_as_seen"),
    path("wallet/", views.wallet, name="wallet"),
]