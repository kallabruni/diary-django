from django.shortcuts import render, get_object_or_404, redirect
from .models import Card
from django.contrib.auth.decorators import login_required
from .forms import CardForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls.base import reverse_lazy
#from django.views.generic.base import TemplateView

@login_required
def all_cards(request):
    get_all = Card.objects.order_by('-card_date_hapend')
    paginator = Paginator(get_all, 10)
    page = request.GET.get('page')
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)
    return render(request, template_name="cards/card.html", context={'page': page, 'cards': cards})

#class AllCards(TemplateView):
#    template_name = "cards/card.html"
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["cards"] = Card.objects.all()
#        return context

@login_required
def new_card(request):
    form = CardForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_cards)
    return render(request, 'cards/new_edit_card.html', {'form': form})

@login_required
def edit_card(request, id):
    card = get_object_or_404(Card, pk=id)
    form = CardForm(request.POST or None, request.FILES or None, instance=card)
    if form.is_valid():
        form.save()
        return redirect(all_cards)
    return render(request, 'cards/new_edit_card.html', {'form': form})

@login_required
def delete_card(request, id):
    card = get_object_or_404(Card, pk=id)
    if request.method == "POST":
        card.delete()
        return redirect(all_cards)
    return render(request, 'cards/delete_card.html', {'card': card})
