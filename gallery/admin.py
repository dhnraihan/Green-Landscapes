from django.contrib import admin
from .models import GalleryCategory, Portfolio, BeforeAfterImage

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'completion_date', 'is_featured')
    list_filter = ('category', 'is_featured', 'completion_date')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'completion_date'
    list_editable = ('is_featured',)
    autocomplete_fields = ('category',)

@admin.register(BeforeAfterImage)
class BeforeAfterImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'completion_date', 'is_featured')
    list_filter = ('category', 'is_featured', 'completion_date')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'completion_date'
    list_editable = ('is_featured',)
    autocomplete_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'description')
        }),
        ('Location & Date', {
            'fields': ('location', 'completion_date')
        }),
        ('Images', {
            'fields': ('before_image', 'after_image')
        }),
        ('Options', {
            'fields': ('is_featured',)
        }),
    )
