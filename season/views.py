from django.shortcuts import render
from rest_framework import generics, permissions, response, status, exceptions
from core.paginate import ExtraSmallResultsSetPagination
from .models import Season
from .serializers import SeasonSerializer


class SeasonListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SeasonSerializer
    queryset = Season.objects.all().order_by('name')
    pagination_class = ExtraSmallResultsSetPagination
