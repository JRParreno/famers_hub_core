from django.shortcuts import render
from rest_framework import generics, permissions, response, status, exceptions
from core.paginate import ExtraSmallResultsSetPagination
from .models import Recommendation
from .serializers import RecommendationSerializer, AddRateSerializer


class RecommendationListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all().order_by('rate', 'title')
    pagination_class = ExtraSmallResultsSetPagination

    def get_queryset(self):
        agriculture_type = self.request.query_params.get('type', None)
        title = self.request.query_params.get('title', None)
        rate = self.request.query_params.get('rate', None)
        if title and agriculture_type and rate:
            return Recommendation.objects.filter(
                title__icontains=title, agriculture_type=agriculture_type,  rate=rate).order_by('rate', 'title')
        if title and agriculture_type:
            return Recommendation.objects.filter(
                title__icontains=title, agriculture_type=agriculture_type).order_by('rate', 'title')

        if agriculture_type:
            return Recommendation.objects.filter(
                agriculture_type=agriculture_type).order_by('rate', 'title')
        # if rate:
        #     return Recommendation.objects.filter(
        #         rate=rate).order_by('rate', 'title')
        if title:
            return Recommendation.objects.filter(
                title__icontains=title).order_by('rate', 'title')
        return Recommendation.objects.all().order_by('rate', 'title')


class RecommendationDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all().order_by('rate', 'title')


class RecommendationRateView(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AddRateSerializer
    queryset = Recommendation.objects.all().order_by('rate', 'title')
