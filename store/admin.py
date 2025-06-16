from django.contrib import admin
from .models import UpComingGames, TrendingGames

# Register your models here.
admin.site.register(UpComingGames)
admin.site.register(TrendingGames)