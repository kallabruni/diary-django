from django.urls import path
from .views import all_cards, new_card, edit_card, delete_card
#from .views import AllCards

urlpatterns = [
    path('', all_cards, name="all_cards"),
    #path("", AllCards.as_view(), name="all_cards"),
    path('new/', new_card, name="new_card"),
    path('edit/<int:id>/', edit_card, name="edit_card"),
    path('delete/<int:id>/', delete_card, name="elete_card"),
]
