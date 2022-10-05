from django.contrib import admin
from .models import PacManPlayer

@admin.register(PacManPlayer)
class PacManPlayerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'school', 'high_score')