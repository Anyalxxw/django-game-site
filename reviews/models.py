from django.db import models
from game_of_the_month.models import Genre

# Create your models here.
class Review(models.Model):
    image = models.ImageField(default='fc25.png')
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)
    rating = models.IntegerField(default=0)
    day = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    def short(self):
        if len(self.description) > 300:
            return self.description[:300] + "..."
        return self.description
        