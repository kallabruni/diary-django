from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["card_title", "card_date_long", "status"]
    list_filter = ["card_date_long", "status"]
    search_fields = ["card_title", "card_date_long", "status"]
