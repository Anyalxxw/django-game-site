from django.shortcuts import redirect, render
from game_of_the_month.models import GameOfTheMonth, Genre
from reviews.models import Review
from blog.models import BlogPost
from library.models import Game

def home(request):
    game = GameOfTheMonth.objects.last()
    reviews = Review.objects.all()[:3]
    posts = BlogPost.objects.all()[:5]
    featured_game = Game.objects.filter(is_main=True).first or Game.objects.first()
    popular_games = Game.objects.all()
    categories = Genre.objects.filter(image__isnull=False)
    return render(request, 'home.html', {
        'game': game,
        'reviews': reviews,
        'posts': posts,
        'featured_game': featured_game,
        'popular_games': popular_games,
        'categories': categories,
    })