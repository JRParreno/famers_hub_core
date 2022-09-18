from django.db import models
from django.utils import timezone

class Insect(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    link = models.TextField()
    insect_image = models.ImageField(upload_to='insect-images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        return super(Insect, self).save(*args, **kwargs)