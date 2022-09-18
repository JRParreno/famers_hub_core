from django.db import models

class Insecticide(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=20, null=True, blank=True)
    link = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name