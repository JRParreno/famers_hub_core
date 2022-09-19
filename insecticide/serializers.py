from rest_framework import serializers
from .models import Insecticide


class InsecticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insecticide
        fields = ['pk', 'name', 'acronym', 'link', 'insecticide_image']
