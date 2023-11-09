from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('auth_token', )

    def get_auth_token(self, obj):
        try:
            token = Token.objects.get(user=obj)
        except Token.DoesNotExist:
            token = Token.objects.create(user=obj)
            print('new token')
        return token.key


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
