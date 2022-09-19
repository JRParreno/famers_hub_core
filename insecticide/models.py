from django.db import models
from django.utils import timezone


class Insecticide(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=20, null=True, blank=True)
    link = models.TextField(blank=True, null=True)
    insecticide_image = models.ImageField(
        upload_to='images/insecticides/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        return super(Insecticide, self).save(*args, **kwargs)
