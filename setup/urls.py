from django.contrib import admin
from django.templatetags import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from setup import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.galeria.urls')), 
    path('', include('apps.usuarios.urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)