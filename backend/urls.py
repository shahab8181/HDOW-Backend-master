from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('client.urls')),
    path('supervisors/',include('supervisor.urls')),
    path('technicians/',include('technician.urls')),
    path('api/base', SpectacularAPIView.as_view(), name='base-swagger-ui'),
    path('swagger/api', SpectacularSwaggerView.as_view(url_name='base-swagger-ui'), name='swagger-ui'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
