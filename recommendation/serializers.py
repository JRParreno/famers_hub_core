from pyexpat import model
from rest_framework import serializers
from .models import Recommendation, RecommendationSeasons
from season.serializers import SeasonSerializer
from agriculture.serializers import AgricultureTypeSerializer
from infestation.serializers import InfestationSerializer
from user_profile.serializers import AuthorSerializer


class RecommendationSeasonsSerializer(serializers.ModelSerializer):
    season = SeasonSerializer()

    class Meta:
        model = RecommendationSeasons
        fields = ['pk', 'season', 'description', 'image']


class RecommendationSerializer(serializers.ModelSerializer):
    agriculture_type = AgricultureTypeSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Recommendation
        fields = ['pk', 'title', 'author', 'rate', 'link', 'agriculture_type']

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(RecommendationSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super(RecommendationSerializer,
                     self).to_representation(instance)

        if 'request' in self.context and self.request:

            seasons = RecommendationSeasonsSerializer(
                instance.recommendation_season.all(), many=True, context={"request": self.request})
            infestations = InfestationSerializer(
                instance.recommendation_infestation.all(), many=True, context={"request": self.request})
            data['seasons'] = seasons.data
            data['infestations'] = infestations.data
        return data


class AddRateSerializer(serializers.ModelSerializer):
    my_rate = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Recommendation
        fields = ['pk', 'my_rate']

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(AddRateSerializer, self).__init__(*args, **kwargs)

    def update(self, instance, validated_data):
        my_rate = validated_data.pop('my_rate', None)

        if my_rate:
            instance.rate += my_rate
            instance.save()
        return super().update(instance, validated_data)
