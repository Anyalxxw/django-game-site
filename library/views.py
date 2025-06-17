from django.shortcuts import render
from .models import Game
from django.http import JsonResponse

# Create your views here.
def get_game_data(request, game_id):
    game = Game.objects.get(pk=game_id)
    return JsonResponse({
        'title': game.title,
        'description': game.description,
        'rating': game.rating,
        'release_date': game.release_date.strftime('%B %d, %Y'),
        'platforms': [p.name for p in game.platforms.all()],
        'genre': [g.name for g in game.genre.all()],
        'image_url': game.image.url,
    })
    