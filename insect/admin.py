from django.contrib import admin
from .models import Insect


@admin.register(Insect)
class InsectAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_updated', 'date_created')
    ordering = ('name', 'date_updated',)
    search_fields = ('name', )
    