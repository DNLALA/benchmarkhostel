from rest_framework import serializers
from hostel.models import Hostel
from users.api.serializers import UserSerializer

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class HostelDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Hostel
        fields = '__all__'