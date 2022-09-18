from django.contrib import admin
from .models import PreventMeasure

@admin.register(PreventMeasure)
class PreventMeasureAdminView(admin.ModelAdmin):
    list_display = ('id', 'description', 'date_created', 'date_updated')
    ordering = ('description', 'date_updated')
    search_fields = ('description',)