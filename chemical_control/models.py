import imp
from django.db import models
from insecticide.models import Insecticide
from infestation.models import Infestation


class ChemicalControl(models.Model):
    LOW = 'LOW'
    MODERATE = 'MODERATE'
    HIGH = 'HIGH'
    NA = 'N/A'

    HAZARD_CHOICES = [
        (LOW, 'Low Toxic'),
        (MODERATE, 'Moderate Toxic'),
        (HIGH, 'High Toxic'),
        (NA, 'N/A'),
    ]

    infestation = models.ForeignKey(Infestation, on_delete=models.CASCADE, related_name='chemical_control_infestation',
                                    null=True, blank=True)
    reminder = models.TextField()
    link = models.TextField(blank=True, null=True)
    hazard_level = models.CharField(
        choices=HAZARD_CHOICES, default=NA, max_length=100)

    def __str__(self):
        return self.reminder


class ChemicalInsecticide(models.Model):
    chemical_control = models.ForeignKey(
        ChemicalControl, on_delete=models.CASCADE, related_name='chemical_control_insecticide')
    insecticide = models.ForeignKey(Insecticide, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.insecticide.name


class ChemicalSafetyPrecaution(models.Model):

    chemical_control = models.ForeignKey(
        ChemicalControl, on_delete=models.CASCADE, related_name='chemical_control_precaution')
    description = models.TextField()
    icon_image = models.ImageField(
        upload_to='images/icons/', null=True, blank=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description


class ChemicalInstruction(models.Model):
    chemical_control = models.ForeignKey(
        ChemicalControl, on_delete=models.CASCADE, related_name='chemical_control_instruction')
    description = models.TextField()
    icon_image = models.ImageField(
        upload_to='images/icons/', null=True, blank=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description
