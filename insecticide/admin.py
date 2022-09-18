from django.contrib import admin
from .models import Insecticide

@admin.register(Insecticide)
class InsecticideAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    ordering = ('name', 'date_updated')
    search_fields = ('name',)