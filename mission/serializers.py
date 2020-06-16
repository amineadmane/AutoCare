from rest_framework import serializers

from .models import Vehicule, Conducteur, Mission, Marque, Modele
from users.models import User
from users.serializers import UserSerializer

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = '__all__'


class ModeleReadSerializer(serializers.ModelSerializer):
    marque = MarqueSerializer()

    class Meta:
        model = Modele
        fields = '__all__'

class ModeleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = '__all__'



class VehiculeReadSerializer(serializers.ModelSerializer):
    modele = ModeleReadSerializer()

    class Meta:
        model = Vehicule
        fields = '__all__'

class VehiculeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'



class ConducteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conducteur
        fields = '__all__'


class MissionReadSerializer(serializers.ModelSerializer):
    vehicule = VehiculeReadSerializer()
    conducteur = ConducteurSerializer()

    class Meta:
        model = Mission
        fields = '__all__'


class MissionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'
