from django.db import models
from insect.models import Insect

class Infestation(models.Model):
    insect = models.ForeignKey(Insect, on_delete=models.CASCADE)
    recommendation = models.TextField()
    organic_control = models.TextField()
    link = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Infestation: {self.recommendation}'


class Symptom(models.Model):
    infestation = models.ForeignKey(Infestation, on_delete=models.CASCADE)
    description = models.TextField()
    link = models.TextField()
    symptom_image = models.ImageField(upload_to='symptom-images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Symptom {self.description}'


class PreventMeasure(models.Model):
    infestation = models.ForeignKey(Infestation, on_delete=models.CASCADE)
    description = models.TextField()
    prevent_image = models.ImageField(upload_to='prevent-images/')
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description