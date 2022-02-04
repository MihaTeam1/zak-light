from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path(r'', include('index.urls'))
]