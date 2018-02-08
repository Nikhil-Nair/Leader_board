# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Score
from .forms import AddScoreForm


class ScoreListView(ListView):
    model = Score
    template_name = 'home.html'

class ScoreDetailView(DetailView):
    model = Score
    template_name = 'score_detail.html'

class ScoreUpdateView(UpdateView):
    model = Score
    fields = ['player_score']
    template_name = 'score_update.html'

class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_delete.html'
    success_url = reverse_lazy('home')

def scoreCreateView(request):
    form = AddScoreForm(request.POST)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.score_admin = request.user
        temp.save()
        return redirect('/')
    return render(request, 'new_score.html', {'form' : form,})


def scoreAdminListView(request, queryset=None):
    object_list = Score.objects.filter(score_admin=request.user)
    context = {
        "object_list" : object_list
    }
    return render(request, 'score_admin_view.html', context)
