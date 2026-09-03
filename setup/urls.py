from django.contrib import admin
from django.templatetags import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from setup import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)