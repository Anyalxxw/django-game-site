from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog-list.html', {'posts': posts})


def blog_details(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/blog-details.html', {'post':post})