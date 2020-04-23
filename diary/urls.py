from django.contrib import admin
from django.urls import path, include
from diary.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('card/', include("cards.urls"))
]
