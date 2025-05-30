from django.contrib import admin
from .models import BookingTimeSlot, BookingStatus, Booking

@admin.register(BookingTimeSlot)
class BookingTimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'get_start_time_display', 'is_available')
    list_filter = ('is_available',)
    list_editable = ('is_available',)
    search_fields = ('start_time',)

@admin.register(BookingStatus)
class BookingStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'date', 'time_slot', 'status', 'created_at')
    list_filter = ('status', 'date', 'service')
    search_fields = ('user__username', 'user__email', 'special_instructions', 'address')
    date_hierarchy = 'date'
    autocomplete_fields = ('user', 'service', 'time_slot', 'status')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'service')
        }),
        ('Schedule', {
            'fields': ('date', 'time_slot')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Additional Information', {
            'fields': ('special_instructions', 'address', 'phone')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user', 'service', 'time_slot', 'status')
