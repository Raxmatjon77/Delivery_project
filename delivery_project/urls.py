from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import landing
urlpatterns = [
    path("",landing ,name="landing"),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
