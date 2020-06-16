from rest_framework import serializers

from .models import RapportSignalProbleme, RapportSignalChauffeur, RapportSignalSinistre

from mission.serializers import VehiculeReadSerializer, ConducteurSerializer

class RapportSignalProbleme_ReadSerializer(serializers.ModelSerializer):
    vehicule = VehiculeReadSerializer()

    class Meta:
        model = RapportSignalProbleme
        fields = '__all__'

class RapportSignalProbleme_WriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportSignalProbleme
        fields = '__all__'



class RapportSignalChauffeur_ReadSerializer(serializers.ModelSerializer):
    conducteur = ConducteurSerializer()

    class Meta:
        model = RapportSignalChauffeur
        fields = '__all__'

class RapportSignalChauffeur_WriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportSignalChauffeur
        fields = '__all__'


class RapportSignalSinistre_ReadSerializer(serializers.ModelSerializer):
    vehicule = VehiculeReadSerializer()
    conducteur = ConducteurSerializer()

    class Meta:
        model = RapportSignalSinistre
        fields = '__all__'


class RapportSignalSinistre_WriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportSignalSinistre
        fields = '__all__'
