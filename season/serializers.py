from pyexpat import model
from rest_framework import serializers
from .models import Season


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = ['pk', 'name', 'description', 'season_image']
