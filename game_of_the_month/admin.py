from django.contrib import admin
from .models import Genre, Platform, GameOfTheMonth

# Register your models here.
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(GameOfTheMonth)
