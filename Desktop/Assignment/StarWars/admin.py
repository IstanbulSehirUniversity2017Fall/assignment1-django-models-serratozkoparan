# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from StarWars.models import StarWarsFilmSeries, Episodes

admin.site.register(StarWarsFilmSeries)
admin.site.register(Episodes)