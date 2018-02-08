from django import forms

from .models import Score

class AddScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = ('name', 'player_score')
