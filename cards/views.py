from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

def all_cards(request):
    get_all_cards = Card.objects.all()
    return render(request, template_name="card.html", context={'cards': get_all_cards})
