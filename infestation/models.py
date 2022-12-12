from django.db import models
from insect.models import Insect
from recommendation.models import Recommendation


class Infestation(models.Model):
    FLOWERING = 'FLOWERING'
    HARVESTING = 'HARVESTING'
    NA = 'N/A'

    STAGES = [
        (FLOWERING, 'Flowering'),
        (HARVESTING, 'Harvesting'),
        (NA, 'N/A'),
    ]

    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE, related_name='recommendation_infestation',
                                       null=True, blank=True)
    insect = models.ForeignKey(Insect, on_delete=models.CASCADE)
    recommendation_description = models.TextField()
    organic_control = models.TextField()
    link = models.TextField()
    insect_stage = models.CharField(choices=STAGES, default=NA, max_length=100)

    def __str__(self):
        return f'Infestation: {self.recommendation}'


class Symptom(models.Model):
    infestation = models.ForeignKey(
        Infestation, on_delete=models.CASCADE, related_name='infestaion_symptom')
    description = models.TextField()
    link = models.TextField()
    symptom_image = models.ImageField(
        upload_to='images/symptoms', null=True, blank=True)

    def __str__(self):
        return f'Symptom {self.description}'


class PreventMeasure(models.Model):
    infestation = models.ForeignKey(
        Infestation, on_delete=models.CASCADE, related_name='infestaion_prevent_measure')
    description = models.TextField()
    link = models.TextField(blank=True, null=True)
    prevent_image = models.ImageField(
        upload_to='images/prevents', null=True, blank=True)

    def __str__(self):
        return self.description
