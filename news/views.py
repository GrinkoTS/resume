from django.shortcuts import render
from .models import Artiles
from django.views.generic import DetailView


def news_home(request):
    firms = Artiles.objects.all()
    return render(request, 'news/news_home.html', {'firms': firms})

class FirmsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'firms'
