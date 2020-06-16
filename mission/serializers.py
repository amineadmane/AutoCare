from rest_framework import serializers

from .models import Vehicule, Conducteur, Mission
from users.models import User
from users.serializers import UserSerializer

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'


class ConducteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conducteur
        fields = '__all__'


class MissionReadSerializer(serializers.ModelSerializer):
    vehicule = VehiculeSerializer()
    conducteur = ConducteurSerializer()

    class Meta:
        model = Mission
        fields = '__all__'


class MissionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'
