from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'price_suffix', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'description', 'short_description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_featured',)
    autocomplete_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'slug', 'description', 'short_description')
        }),
        ('Pricing', {
            'fields': ('price', 'price_suffix')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Options', {
            'fields': ('is_featured',)
        }),
    )
