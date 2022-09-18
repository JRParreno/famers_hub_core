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
    list_display = ('id', 'author', 'name')
    ordering = ('author', 'name')
    search_fields = ('author', 'name')
    inlines = [RecommendationSeasonsAdminInline, InfestationAdminInline]