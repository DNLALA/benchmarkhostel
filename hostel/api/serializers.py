from rest_framework import serializers
from hostel.models import Hostel, Transfar, Request
from users.api.serializers import UserSerializer


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class TransfarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfar
        fields = '__all__'



class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class HostelDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Hostel
        fields = '__all__'