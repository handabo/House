from api.serializers import HouseTypeSerializer
from rest_framework import viewsets
from common.models import HouseType


class HouseTypeViewSet(viewsets.ModelViewSet):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer
    pagination_class = None