from django.db import models
from game_of_the_month.models import Platform,Genre

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    platforms = models.ManyToManyField(Platform)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(default='fc25.png')
    cover = models.ImageField(null=True, blank=True,default='fc25.png')
    is_main = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
    