from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    #fields = ["tytul", "opis", "rok"]
    #exclude = ["opis"]
    list_display = ["card_title", "card_date_long"]
    list_filter = ["card_date_long"]
    #search_fields = ["tytul", "opis"]
