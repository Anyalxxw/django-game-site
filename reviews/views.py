from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Review

# Create your views here.
def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/reviews_list.html', {"reviews": reviews})

def review_details(request, id):
    review = get_object_or_404(Review, pk = id)
    return render(request, 'reviews/review_details.html', {'review': review})