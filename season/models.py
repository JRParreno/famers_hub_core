from django.db import models

class Season(models.Model):
    DRY = 'DRY'
    WET = 'WET'
    NA = 'N/A'

    SEASON_CHOICES = [
        (DRY, 'Dry Season'),
        (WET, 'Wet Season'),
        (NA, 'N/A'),
    ]

    name = models.CharField(choices=SEASON_CHOICES, default=NA, max_length=100)
    description = models.TextField()
    season_image = models.ImageField(upload_to='season-images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name