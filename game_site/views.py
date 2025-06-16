from django.shortcuts import redirect, render
from game_of_the_month.models import GameOfTheMonth
from reviews.models import Review
from blog.models import BlogPost

def home(request):
    game = GameOfTheMonth.objects.last()
    reviews = Review.objects.all()[:3]
    posts = BlogPost.objects.all()[:5]
    return render(request, 'home.html', {
        'game': game,
        'reviews': reviews,
        'posts': posts,
    })