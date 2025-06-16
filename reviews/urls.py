from django.urls import path, include
from . import views

app_name="reviews"

urlpatterns = [
    path('', views.reviews_list, name='reviews_list'),
    path('<int:id>/', views.review_details, name='review_details')
]
