# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StarWarsFilmSeries(models.Model):
    creator = models.CharField(max_length=50)
    genre = models.CharField(max_length=200)

class Episodes(models.Model):
    starwars = models.ForeignKey(StarWarsFilmSeries, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    IMDB_rate = models.IntegerField()