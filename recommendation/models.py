from django.db import models
from user_profile.models import UserProfile
from agriculture.models import AgricultureType
from season.models import Season
from django.utils import timezone


class Recommendation(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    agriculture_type = models.ForeignKey(
        AgricultureType, on_delete=models.CASCADE, related_name='agriculture_type', parent_link=True,)
    link = models.TextField()

    def __str__(self):
        return self.name

    def agriculture_type_name(self):
        return self.agriculture_type.name
    agriculture_type_name.short_description = 'Agriculture Name'


class RecommendationSeasons(models.Model):
    recommendation = models.ForeignKey(
        Recommendation, on_delete=models.CASCADE, related_name='recommendation_season')
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='recommendation_season')
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/recommendation-season-photos/', blank=True, null=True)

    def __str__(self) -> str:
        return self.description
