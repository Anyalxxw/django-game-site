from django.shortcuts import render
from django.http import HttpResponse
from .models import UpComingGames,TrendingGames

# Create your views here.
def store_list(request):
    games = UpComingGames.objects.all()
    trendgames = TrendingGames.objects.all()
    return render(request, 'store/store_list.html', {
        "games": games,
        "trendgames": trendgames,
        })