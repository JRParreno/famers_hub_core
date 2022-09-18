import imp
from django.db import models
from insecticide.models import Insecticide
from infestation.models import Infestation

class ChemicalControl(models.Model):
    infestation = models.ForeignKey(Infestation, on_delete=models.CASCADE)
    reminder = models.TextField()
    link = models.TextField(blank=True, null=True)
    percentage = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.reminder

class ChemicalInsecticide(models.Model):
    chemical_control = models.ForeignKey(ChemicalControl, on_delete=models.CASCADE)
    insecticide = models.ForeignKey(Insecticide, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.insecticide.name

class ChemicalSafetyPrecaution(models.Model):
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

    chemical_control = models.ForeignKey(ChemicalControl, on_delete=models.CASCADE)
    description = models.TextField()
    icon_image = models.ImageField(upload_to='icon-images/')
    link = models.TextField(blank=True, null=True)
    hazard_level = models.CharField(choices=HAZARD_CHOICES, default=NA, max_length=100)

    def __str__(self):
        return self.description


class ChemicalInstruction(models.Model):
    chemical_control = models.ForeignKey(ChemicalControl, on_delete=models.CASCADE)
    description = models.TextField()
    icon_image = models.ImageField(upload_to='icon-images/')
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description