from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator

from .models import UserProfile
from .forms import UserProfileForm, CustomUserCreationForm
from bookings.models import Booking

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('core:home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Account created successfully. Welcome!')
        return redirect('core:home')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')
    
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

class CustomLogoutView(View):
    """
    Custom logout view that handles both GET and POST requests
    and shows a confirmation page before logging out.
    """
    def get(self, request, *args, **kwargs):
        # Show confirmation page
        return render(request, 'registration/logout_confirm.html')
    
    def post(self, request, *args, **kwargs):
        # Log the user out and redirect to the logged out page
        logout(request)
        return render(request, 'registration/logged_out.html')
