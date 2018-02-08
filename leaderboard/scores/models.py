# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    class Meta:
            ordering = ['-player_score']
    score_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,primary_key=True)
    player_score = models.IntegerField()

    def get_absolute_url(self):
        return reverse('home')

    def filterByAdmin(self):
        return Score.objects.get(score_admin=User.username)

    def __str__(self):
        return self.name
