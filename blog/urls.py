from django.urls import path, include
from . import views

app_name='blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<slug:slug>/',views.blog_details, name='blog-details'),
]
