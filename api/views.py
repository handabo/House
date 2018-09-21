from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

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


@api_view(['GET'])
def districts(request, pid):
    query_set = District.objects.filter(parent__distid=pid)
    serializer = DistrictSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "page"
    page_size_query_param = "size"


class EstateView(ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

    def get(self, request, distid, *args, **kwargs):
        query_set = Estate.objects.filter(district__distid=distid)
        pager = MyPageNumberPagination()
        paged_query_set = pager.paginate_queryset(
            queryset=query_set, request=request, view=self)
        return pager.get_paginated_response(
            EstateSerializer(paged_query_set, many=True).data)