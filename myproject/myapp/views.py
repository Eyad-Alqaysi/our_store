from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic
from .models import Game, Developer

def index(request):
    # Simple context for now, you can add more details later
    return render(request, 'index.html')

class GameListView(generic.ListView):
    model = Game
    template_name = 'games/game_list.html'

class DeveloperListView(generic.ListView):
    model = Developer
    template_name = 'developers/developer_list.html'

class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'myapp/game_detail.html'  # Correct path based on your app's name


class DeveloperDetailView(generic.DetailView):
    model = Developer
    template_name = 'developers/developer_detail.html'
