import os
import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

def get_upload_path(instance, filename):
    """Generate a random filename for uploaded files."""
    ext = filename.split('.')[-1].lower()
    # Create a random filename using UUID
    filename = f"{uuid.uuid4().hex}.{ext}"
    # Create a path with first two characters of the filename as subdirectories
    return os.path.join('services', filename[0:2], filename[2:4], filename)

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Service Categories"

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Leave blank if price varies")
    price_suffix = models.CharField(max_length=20, blank=True, help_text="e.g. 'per hour', 'per visit'")
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.short_description and self.description:
            # Set short description to first 100 chars of description if not provided
            self.short_description = self.description[:100] + '...' if len(self.description) > 100 else self.description
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.name
