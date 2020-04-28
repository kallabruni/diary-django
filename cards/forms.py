from django.forms import ModelForm
from .models import Card

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['card_images', 'card_title', 'card_description']
