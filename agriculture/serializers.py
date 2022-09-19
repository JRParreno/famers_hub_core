from pyexpat import model
from rest_framework import serializers
from .models import Agriculture, AgricultureType


class AgricultureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agriculture
        fields = ['pk', 'name', 'description', 'agriculture_image']


class AgricultureTypeSerializer(serializers.ModelSerializer):
    agriculture = AgricultureSerializer()

    class Meta:
        model = AgricultureType
        fields = ['pk', 'name', 'description',
                  'agriculture_type_image',
                  'agriculture',
                  ]
