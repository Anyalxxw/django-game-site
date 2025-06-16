from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
    # short def