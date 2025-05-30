from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('category/<slug:slug>/', views.GalleryCategoryView.as_view(), name='gallery_category'),
    path('before-after/', views.BeforeAfterView.as_view(), name='before_after'),
]
