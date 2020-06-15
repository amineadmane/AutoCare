from rest_framework import serializers
from .models import User, Admin, RegionalUser, OperationnelUser, CentralUser


class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='get_user_type_display')
    class Meta:
        model = User
        fields = ['id', 'username', 'user_type', 'profile_id', 'first_name', 'last_name',
                  'nss','dateNaissance','tel','grade','dateEmbauche','region','unite','service']


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'user_type', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        first_name = ""
        last_name = ""
        if "first_name" in self.validated_data:
            first_name=self.validated_data['first_name']
        if "last_name" in self.validated_data:
            last_name=self.validated_data['last_name']
        user = User(username=self.validated_data['username'],user_type=self.validated_data['user_type'],first_name=first_name,last_name=last_name)

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
