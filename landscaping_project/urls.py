"""
URL configuration for landscaping_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('services/', include(('services.urls', 'services'), namespace='services')),
    path('gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    path('bookings/', include(('bookings.urls', 'bookings'), namespace='bookings')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth views
]

# Add media URL mapping in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Register custom error handlers
handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'
