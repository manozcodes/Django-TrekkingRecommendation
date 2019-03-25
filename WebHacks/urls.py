from django.contrib import admin
from django.urls import include
from django.urls import path
from blog import burl
from django.conf.urls.static import static
from WebHacks import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(burl)),
    path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
