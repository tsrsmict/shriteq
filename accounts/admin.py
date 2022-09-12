from accounts.models import School
from django.contrib import admin

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    # list_display = ('display_name', 'question', 'date_modified')
    list_display = ('display_name', 'date_modified')
