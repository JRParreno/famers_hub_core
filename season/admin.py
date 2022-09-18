from django.contrib import admin
from .models import Season
from django.contrib.auth.models import Group

# remove group from admin
admin.site.unregister(Group)

@admin.register(Season)
class SeasonAdminView(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('name',)
    search_fields = ('name',)
