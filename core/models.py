import os
import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def get_testimonial_image_path(instance, filename):
    """Generate a random filename for testimonial images."""
    ext = filename.split('.')[-1].lower()
    # Create a random filename using UUID
    filename = f"{uuid.uuid4().hex}.{ext}"
    # Create a path with first two characters of the filename as subdirectories
    return os.path.join('testimonials', filename[0:2], filename[2:4], filename)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, help_text="e.g. 'Homeowner', 'Business Owner'")
    company = models.CharField(max_length=100, blank=True)
    testimonial = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)
    image = models.ImageField(upload_to=get_testimonial_image_path, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.rating} stars"
    
    class Meta:
        ordering = ['-is_featured', '-created_at']

class ContactSubmission(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.subject} from {self.name}"
    
    class Meta:
        ordering = ['-created_at']

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="The order in which this FAQ appears (lower numbers appear first)")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
