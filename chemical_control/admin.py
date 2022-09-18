from django.contrib import admin
from .models import ChemicalControl, ChemicalInsecticide, ChemicalSafetyPrecaution, ChemicalInstruction


class SafetyPrecautionAdminInline(admin.StackedInline):
    model = ChemicalSafetyPrecaution
    max_num = 20
    extra = 1

class ChemicalInsecticideAdminInline(admin.StackedInline):
    model = ChemicalInsecticide
    max_num = 20
    extra = 1

class ChemicalInstructionAdminInline(admin.StackedInline):
    model = ChemicalInstruction
    max_num = 20
    extra = 1

@admin.register(ChemicalControl)
class ChemicalControlAdminView(admin.ModelAdmin):
    list_display = ('id', 'reminder',)
    ordering = ('reminder',)
    search_fields = ('reminder', )
    inlines = [ChemicalInsecticideAdminInline, SafetyPrecautionAdminInline, ChemicalInstructionAdminInline]