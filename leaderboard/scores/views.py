# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Score

class ScoreListView(ListView):
    model = Score
    template_name = 'home.html'

class ScoreDetailView(DetailView):
    model = Score
    template_name = 'score_detail.html'

class ScoreCreateView(CreateView):
    model = Score
    template_name = 'new_score.html'
    fields = '__all__'

class ScoreUpdateView(UpdateView):
    model = Score
    fields = ['player_score']
    template_name = 'score_update.html'

class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_delete.html'
    success_url = reverse_lazy('home')
