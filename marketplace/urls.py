from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from core.views import index, about, privacy_policy, terms_of_use

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('about/', about, name='about'),
    path('policy/', privacy_policy, name='policy'),
    path('terms/', terms_of_use, name='terms'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
