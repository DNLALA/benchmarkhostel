from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.api.urls')),
    path('hostel/', include('hostel.api.urls')),
]
