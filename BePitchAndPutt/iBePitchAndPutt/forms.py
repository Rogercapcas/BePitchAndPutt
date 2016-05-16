from django.forms import ModelForm
from models import Match, Throw

class MatchForm(ModelForm):
    class Meta:
        model = Match
        exclude = ('match_number', 'date', 'weather',)

class TrowForm(ModelForm):
	class Meta:
		model = Throw
		exclude = ('match',)