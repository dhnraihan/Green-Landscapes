from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone

from .models import UserProfile
from .forms import UserProfileForm, CustomUserCreationForm
from bookings.models import Booking

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Account created successfully. Welcome!')
        return redirect('home')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        # Get the current user's profile
        return self.request.user.profile
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get user bookings
        context['upcoming_bookings'] = Booking.objects.filter(
            user=self.request.user,
            date__gte=timezone.now().date()
        ).order_by('date', 'time_slot__start_time')[:5]
        
        # Get completed bookings
        context['completed_bookings'] = Booking.objects.filter(
            user=self.request.user,
            status__name='completed'
        ).order_by('-date')[:5]
        
        return context
