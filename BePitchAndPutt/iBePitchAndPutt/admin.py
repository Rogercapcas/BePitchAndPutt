from django.contrib import admin
from .models import Player, Match, Field, Hole
# Register your models here.

admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Field)
admin.site.register(Hole)
