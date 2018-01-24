# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Score(models.Model):
    class Meta:
            ordering = ['-player_score']

    name = models.CharField(max_length=100,primary_key=True)
    player_score = models.IntegerField()

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
