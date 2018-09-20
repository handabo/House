from rest_framework import serializers

from common.models import District
from common.models import HouseType
from common.models import Estate


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('distid', 'name', 'intro')


class HouseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseType
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estate
        fields = ('estateid', 'district', 'name')
