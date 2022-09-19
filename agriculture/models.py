from django.db import models
from django.utils import timezone


class Agriculture(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    agriculture_image = models.ImageField(
        upload_to='images/agriculture/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        return super(Agriculture, self).save(*args, **kwargs)


class AgricultureType(models.Model):
    agriculture = models.ForeignKey(
        Agriculture, on_delete=models.CASCADE, related_name='agriculture_sub')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    agriculture_type_image = models.ImageField(
        upload_to='images/agriculture-type/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.agriculture.name}'

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        return super(AgricultureType, self).save(*args, **kwargs)
