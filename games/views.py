from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Game


class GamesListView(ListView):
    template_name = "game_list.html"
    model = Game
    context_object_name = "games"


class GamesDetailView(DetailView):
    template_name = "game_detail.html"
    model = Game
