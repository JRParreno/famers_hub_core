from django.contrib import admin
from recommendation.models import RecommendationSeasons
from infestation.models import Infestation, Recommendation


class InfestationAdminInline(admin.StackedInline):
    model = Infestation
    max_num = 20
    extra = 1
    show_change_link = True


class RecommendationSeasonsAdminInline(admin.TabularInline):
    model = RecommendationSeasons
    max_num = 20
    extra = 1


@admin.register(Recommendation)
class RecommendationAdminView(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'agriculture_type_name')
    ordering = ('author', 'title')
    search_fields = ('author', 'title')
    inlines = [RecommendationSeasonsAdminInline, InfestationAdminInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'agriculture_type')
        }),
    )
