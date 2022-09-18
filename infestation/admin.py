from django.contrib import admin
from chemical_control.models import ChemicalControl
from .models import Infestation, PreventMeasure, Symptom

class ChemicalControlAdminInline(admin.StackedInline):
    model = ChemicalControl
    max_num = 20
    extra = 1


class PreventMeasureAdminInline(admin.StackedInline):
    model = PreventMeasure
    max_num = 20
    extra = 1


class SymptomAdminInline(admin.StackedInline):
    model = Symptom
    max_num = 20
    extra = 1


@admin.register(Infestation)
class InfestationAdminView(admin.ModelAdmin):
    list_display = ('id', 'insect', 'recommendation')
    ordering = ('insect',)
    search_fields = ('insect', 'recommendation')
    inlines = [ChemicalControlAdminInline, PreventMeasureAdminInline, SymptomAdminInline]