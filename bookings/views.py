from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse

from .models import Booking, BookingTimeSlot, BookingStatus
from services.models import Service
from .forms import BookingForm

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_create.html'
    success_url = reverse_lazy('booking_success')
    
    def get_initial(self):
        initial = super().get_initial()
        if 'service_id' in self.kwargs:
            initial['service'] = self.kwargs['service_id']
        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['time_slots'] = BookingTimeSlot.objects.filter(is_available=True)
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        # Set default status to pending (assuming 1 is the ID for 'pending')
        try:
            pending_status = BookingStatus.objects.get(name='pending')
            form.instance.status = pending_status
        except BookingStatus.DoesNotExist:
            # Create the pending status if it doesn't exist
            pending_status = BookingStatus.objects.create(name='pending', description='Booking is awaiting confirmation')
            form.instance.status = pending_status
        
        # Check if the time slot is already booked for that date
        date = form.cleaned_data['date']
        time_slot = form.cleaned_data['time_slot']
        
        if Booking.objects.filter(date=date, time_slot=time_slot).exists():
            form.add_error('time_slot', 'This time slot is already booked for the selected date')
            return self.form_invalid(form)
        
        messages.success(self.request, 'Your booking has been created successfully!')
        return super().form_valid(form)

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_bookings'] = self.get_queryset().filter(
            date__gte=timezone.now().date(),
            status__name__in=['pending', 'confirmed']
        )
        context['past_bookings'] = self.get_queryset().filter(
            date__lt=timezone.now().date()
        )
        return context

class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'booking'
    
    def get_queryset(self):
        # Ensure users can only view their own bookings
        return Booking.objects.filter(user=self.request.user)

class BookingSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'bookings/booking_success.html'

# API view to check available time slots for a given date
def get_available_time_slots(request):
    date = request.GET.get('date')
    if not date:
        return JsonResponse({'error': 'Date is required'}, status=400)
    
    # Get all time slots
    all_time_slots = BookingTimeSlot.objects.all()
    
    # Get booked time slots for the date
    booked_slots = Booking.objects.filter(date=date).values_list('time_slot_id', flat=True)
    
    # Filter available time slots
    available_slots = all_time_slots.exclude(id__in=booked_slots)
    
    data = {
        'time_slots': [
            {
                'id': slot.id,
                'time': slot.get_start_time_display()
            } for slot in available_slots
        ]
    }
    
    return JsonResponse(data)
