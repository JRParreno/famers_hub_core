from django.db import models

class PreventMeasure(models.Model):

    description = models.TextField()
    prevent_image = models.ImageField(upload_to='prevent-images/')
    link = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description