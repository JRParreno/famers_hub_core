from django.shortcuts import render
from rest_framework import generics, permissions, response, status, exceptions
from core.paginate import ExtraSmallResultsSetPagination
from .models import Recommendation
from .serializers import RecommendationSerializer


class RecommendationListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all().order_by('name')
    pagination_class = ExtraSmallResultsSetPagination


class RecommendationDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all().order_by('name')
