from django.contrib import admin
from .models import PlayerDynamicData, PlayerDynamicDataRanks

# Register your models here.

admin.site.register(PlayerDynamicData)
admin.site.register(PlayerDynamicDataRanks)