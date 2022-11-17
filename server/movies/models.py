from django.db import models
# from django.contrib.postgres.fields import ArrayField 

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64)

class Keyword(models.Model):
    name = models.CharField(max_length=128)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    release_date = models.CharField(max_length=128)
    vote_average = models.FloatField()
    overview = models.TextField()
    backdrop_path = models.TextField()
    paster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movie_genres')
    keywords = models.ManyToManyField(Keyword, related_name='movie_keywords', blank=True)
    director = models.CharField(max_length=512, blank=True)
    cast = models.CharField(max_length=512, blank=True)
    vote_average_naver = models.FloatField(blank=True)
    link_naver = models.TextField()




