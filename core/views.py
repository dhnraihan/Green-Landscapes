from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from django.contrib import messages
from django.urls import reverse_lazy

from services.models import Service, ServiceCategory
from gallery.models import Portfolio, BeforeAfterImage
from .models import Testimonial, FAQ, ContactSubmission
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_services'] = Service.objects.filter(is_featured=True)[:3]
        context['service_categories'] = ServiceCategory.objects.all()[:6]
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)[:3]
        context['featured_projects'] = Portfolio.objects.filter(is_featured=True)[:4]
        context['before_after'] = BeforeAfterImage.objects.filter(is_featured=True).first()
        return context

class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        # Create a contact submission
        ContactSubmission.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
        )
        messages.success(self.request, 'Your message has been sent. We\'ll get back to you soon!')
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'core/contact_success.html'

class FAQView(ListView):
    template_name = 'core/faq.html'
    model = FAQ
    context_object_name = 'faqs'
    
    def get_queryset(self):
        return FAQ.objects.filter(is_active=True)

def error_404(request, exception):
    return render(request, 'core/404.html', status=404)

def error_500(request):
    return render(request, 'core/500.html', status=500)
