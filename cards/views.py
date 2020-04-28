from django.shortcuts import render, get_object_or_404
from .models import Card
from django.contrib.auth.decorators import login_required
from .forms import CardForm

@login_required
def all_cards(request):
    get_all_cards = Card.objects.order_by('-card_date_long')
    return render(request, template_name="cards/card.html", context={'cards': get_all_cards})

@login_required
def new_card(request):
    form = CardForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'cards/new_edit_card.html', {'form': form})

@login_required
def edit_card(request):
    card = get_object_or_404(Card, pk=id)
    form = CardForm(request.POST or None, request.FILES or None, instance=card)
    if form.is_valid():
        form.save()
    return render(request, 'cards/new_edit_card.html', {'form': form})
