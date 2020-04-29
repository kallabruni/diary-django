from django.contrib import admin
from django.urls import path, include
from diary.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cards/', include("cards.urls")),
    path('auccount/', include("account.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
