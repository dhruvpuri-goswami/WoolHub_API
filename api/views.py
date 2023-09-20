from rest_framework import generics
from .models import RawWoolData
from .serializers import RawWoolDataSerializer
from .filters import RawWoolDataFilter
from django_filters.rest_framework import DjangoFilterBackend

class RawWoolDataListCreate(generics.ListCreateAPIView):
    queryset = RawWoolData.objects.all()
    serializer_class = RawWoolDataSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RawWoolDataFilter
