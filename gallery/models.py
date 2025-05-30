from django.db import models
from django.utils.text import slugify

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Gallery Categories"

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='portfolio_items')
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    completion_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-completion_date', '-created_at']

class BeforeAfterImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='before_after_images')
    before_image = models.ImageField(upload_to='before_after/before/', null=True, blank=True)
    after_image = models.ImageField(upload_to='before_after/after/', null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    completion_date = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-completion_date', '-created_at']
        verbose_name_plural = "Before/After Images"
