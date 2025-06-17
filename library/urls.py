from django.urls import path, include
from . import views

urlpatterns = [
    path('api/game/<int:game_id>/', views.get_game_data, name='get_game_data')
]
