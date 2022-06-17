from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from src.chat import views
from .views import index, profile
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from src.messenger.forms import CustomAuthForm

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('exit/', views.exit, name='exit'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=CustomAuthForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='profile')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

