from django.contrib import admin
from .models import User, Room, Booking

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'phone']
    list_filter = ['is_staff', 'is_active']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'room_type', 'capacity', 'price']
    list_filter = ['room_type']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'room', 'date', 'payment', 'status', 'created_at']
    list_filter = ['status', 'payment']
    list_editable = ['status']
    search_fields = ['user__username', 'user__full_name']