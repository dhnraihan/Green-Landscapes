from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.BookingCreateView.as_view(), name='bookings'),
    path('service/<int:service_id>/', views.BookingCreateView.as_view(), name='book_service'),
    path('list/', views.BookingListView.as_view(), name='booking_list'),
    path('detail/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('success/', views.BookingSuccessView.as_view(), name='booking_success'),
    path('api/available-time-slots/', views.get_available_time_slots, name='api_available_time_slots'),
]
