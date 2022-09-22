from django.shortcuts import render
from rest_framework import generics, permissions, response, status, exceptions
from core.paginate import ExtraSmallResultsSetPagination
from .models import AgricultureType, Agriculture
from .serializers import AgricultureSerializer, AgricultureTypeSerializer


class AgricultureListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AgricultureSerializer
    queryset = Agriculture.objects.all().order_by('name')
    pagination_class = ExtraSmallResultsSetPagination


class AgricultureTypeListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AgricultureTypeSerializer
    queryset = AgricultureType.objects.all().order_by('name')
    pagination_class = ExtraSmallResultsSetPagination

    def get_queryset(self):
        agriculture_pk = self.request.query_params.get('agriculture_pk', None)
        if agriculture_pk:
            return AgricultureType.objects.filter(
                agriculture=agriculture_pk)

        error = {
            "error_message": "Agriculture Type not found"
        }
        raise exceptions.ValidationError(
            detail=error, code=status.HTTP_400_BAD_REQUEST)
