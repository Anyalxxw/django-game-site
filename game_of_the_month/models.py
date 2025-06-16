from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='fc25.png')
    slug = models.SlugField(unique=True, null=True)
    
    def __str__(self):
        return self.name
    

class GameOfTheMonth(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='fc25.png')
    description = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()
    platforms = models.ManyToManyField(Platform)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
