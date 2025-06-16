from django.db import models
from game_of_the_month.models import Genre

# Create your models here.
class UpComingGames(models.Model):
    image = models.ImageField(default='fc25.png')
    title = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    
class TrendingGames(models.Model):
    image = models.ImageField(default='fc25.png')
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    first_price = models.IntegerField(blank=True, null=True, default=0)
    second_price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0, blank=True,null=True)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    