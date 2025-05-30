from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Portfolio, BeforeAfterImage, GalleryCategory

class GalleryView(ListView):
    model = Portfolio
    template_name = 'gallery/gallery.html'
    context_object_name = 'projects'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        context['before_after_images'] = BeforeAfterImage.objects.filter(is_featured=True)[:4]
        return context

class GalleryCategoryView(ListView):
    model = Portfolio
    template_name = 'gallery/gallery_category.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        self.category = get_object_or_404(GalleryCategory, slug=self.kwargs['slug'])
        return Portfolio.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = GalleryCategory.objects.all()
        context['before_after_images'] = BeforeAfterImage.objects.filter(category=self.category)
        return context

class BeforeAfterView(ListView):
    model = BeforeAfterImage
    template_name = 'gallery/before_after.html'
    context_object_name = 'before_after_images'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        return context
