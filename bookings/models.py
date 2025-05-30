from django.db import models
from django.conf import settings
from services.models import Service

class BookingTimeSlot(models.Model):
    TIME_CHOICES = [
        ('08:00', '8:00 AM'),
        ('09:00', '9:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '1:00 PM'),
        ('14:00', '2:00 PM'),
        ('15:00', '3:00 PM'),
        ('16:00', '4:00 PM'),
        ('17:00', '5:00 PM'),
    ]
    
    start_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.get_start_time_display()

class BookingStatus(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    name = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.get_name_display()
    
    class Meta:
        verbose_name_plural = "Booking Statuses"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time_slot = models.ForeignKey(BookingTimeSlot, on_delete=models.CASCADE, related_name='bookings')
    status = models.ForeignKey(BookingStatus, on_delete=models.CASCADE, default=1)  # Default to 'Pending'
    special_instructions = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True, help_text="If different from your account address")
    phone = models.CharField(max_length=15, blank=True, null=True, help_text="If different from your account phone")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.service.name} - {self.date} {self.time_slot}"
    
    class Meta:
        ordering = ['-date', '-time_slot__start_time']
        # Ensure a time slot can only be booked once per day
        unique_together = ['date', 'time_slot']
