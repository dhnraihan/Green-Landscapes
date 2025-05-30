from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Service, ServiceCategory
from gallery.models import Portfolio

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ServiceCategory.objects.all()
        return context

class ServiceCategoryView(ListView):
    model = Service
    template_name = 'services/service_category.html'
    context_object_name = 'services'
    
    def get_queryset(self):
        self.category = get_object_or_404(ServiceCategory, slug=self.kwargs['slug'])
        return Service.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = ServiceCategory.objects.all()
        return context

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related projects that might showcase this service
        service = self.get_object()
        
        # Get related services first
        context['related_services'] = Service.objects.filter(
            category=service.category
        ).exclude(id=service.id)[:3]
        
        # Get portfolio items that match the service's category
        # Note: This assumes there's a relationship between service categories and portfolio categories
        # If needed, you can modify this to match your actual data model
        context['related_projects'] = Portfolio.objects.filter(
            category__name__iexact=service.category.name
        )[:4]
        
        return context
