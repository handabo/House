from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view

from api.serializers import HouseTypeSerializer
from api.serializers import DistrictSerializer
from api.serializers import EstateSerializer

from common.models import HouseType
from common.models import District
from common.models import Estate
from common.models import HouseType


class HouseTypeViewSet(viewsets.ModelViewSet):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer
    pagination_class = None


@api_view(['GET'])
def provinces(request):
    query_set = District.objects.filter(parent__isnull=True)
    serializer = DistrictSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)