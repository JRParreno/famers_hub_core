from rest_framework import serializers
from .models import Insect


class InsectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insect
        fields = ['pk', 'name', 'insect_image', 'link']
