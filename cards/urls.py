from django.urls import path
from .views import all_cards, new_card, edit_card

urlpatterns = [
    path('', all_cards, name="all_cards"),
    path('new_card/', new_card, name="new_card"),
    path('edit_card/<int:id>/', edit_card, name="edit_card")
]
