from django.contrib import admin
from .models import Team, Region, Player, Fixture, Position, Dreamteam, Gameweek

# Register your models here.
admin.site.register(Team)
admin.site.register(Region)
admin.site.register(Player)
admin.site.register(Fixture)
admin.site.register(Position)
admin.site.register(Dreamteam)
admin.site.register(Gameweek)