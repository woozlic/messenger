from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from chat import views
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
    path('exit/', views.exit, name='exit')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
