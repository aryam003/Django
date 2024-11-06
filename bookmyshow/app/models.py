from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name=models.TextField()
    bg_img=models.FileField()
    fb_img=models.FileField()
    duration=models.TextField()
    category=models.TextField()
    date=models.DateField()

    
    def __str__(self):
        return self.movie_name

class Language(models.Model):
    movie_lg=models.TextField()

class Movie_lang(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    l=models.ForeignKey(Language,on_delete=models.CASCADE)    