from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
import chat
from .views import index, profile
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('exit/', chat.views.exit, name='exit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='profile')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
