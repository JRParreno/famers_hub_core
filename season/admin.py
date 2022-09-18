from django.contrib import admin
from .models import Season
from django.contrib.auth.models import Group

# remove group from admin
admin.site.unregister(Group)

@admin.register(Season)
class SeasonAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created', 'date_updated')
    ordering = ('name', 'date_updated')
    search_fields = ('name',)

    def has_add_permission(self, request, obj=None):
        return False