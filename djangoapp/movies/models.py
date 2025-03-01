from django.db import models


class Movies(models.Model):
    Title = models.CharField(max_length=200)
    Rated = models.CharField(max_length=10)
    Released = models.CharField(max_length=20)
    Genre = models.CharField(max_length=50)
    Director = models.CharField(max_length=50)
    Actors = models.CharField(max_length=200)
    Writer = models.CharField(max_length=200)
    Plot = models.CharField(max_length=500)
    Awards = models.CharField(max_length=200)
    Poster = models.CharField(max_length=200)
    imdbRating = models.CharField(max_length=5)
    Type = models.CharField(max_length=20)

    def __str__(self):
        return ('Id: ' + str(self.id) + ' - Filme: ' + self.Title) 