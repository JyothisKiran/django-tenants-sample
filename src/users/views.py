from django.contrib.auth import authenticate, logout
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer, UserLoginSerializer, AuthUserSerializer


class UserModelViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer(self, *args, **kwargs):
        if self.action == 'login':
            print('hi')
            return UserLoginSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    @action(['POST',], detail=False)
    def login(self, request):
        print(request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data['username']
        password = serializer.data['password']
        user = authenticate(username=username,  password=password)
        if user is None:
            return Response("Invalid Credentials")
        data = AuthUserSerializer(user).data
        return Response(data=data)

    @action(['GET', ], detail=False)
    def logout_user(self, request):
        if not request.user:
            return Response("Please Login")
        logout(request.user)
        return Response("sucessfully logged Out")
