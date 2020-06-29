from rest_framework import serializers

from .models import Piece, Guide_constructure, Guide_personnel
from users.models import User
from users.serializers import UserSerializer


class PieceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'

class PieceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'

######################################################################

class Guide_constructureReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide_constructure
        fields = '__all__'

class Guide_constructureWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide_constructure
        fields = '__all__'

########################################################################

class Guide_personnelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide_personnel
        fields = '__all__'

class Guide_personnelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide_personnel
        fields = '__all__'


