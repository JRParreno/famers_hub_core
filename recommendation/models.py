from django.db import models
from user_profile.models import UserProfile
from agriculture.models import Agriculture
from season.models import Season
from django.utils import timezone

class Recommendation(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    agriculture_type = models.ForeignKey(Agriculture, on_delete=models.CASCADE)
    link = models.TextField()
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.date_created = timezone.now()
    #     self.date_updated = timezone.now()
    #     return super(Recommendation, self).save(*args, **kwargs)


class RecommendationSeasons(models.Model):
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE, related_name='recommendation_season')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='recommendation_season')
    description = models.TextField()
    image =  models.ImageField(
        upload_to='images/recommendation-season-photos/', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.description