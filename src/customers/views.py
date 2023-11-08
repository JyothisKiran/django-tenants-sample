from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer, UserLoginSerializer,UsernameSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection
from .models import Client
from django_tenants.utils import get_tenant_model

# Create your views here.


class UserModelViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(client=self.request.tenant)
        return super().perform_create(serializer)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'find_domain':
            print('hi')
            return UsernameSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)
    

    @action(['POST',], detail=False)
    def find_domain(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(str(**serializer.data))
        username = serializer.data['username']
        user_obj = User.objects.get(username=username)
        client = user_obj.client
        print(client)
        if client == 'tenant1':
            redirect_url = 'http://fonzy.localhost:8000/au/u/users/login'
        else:
            print("redirecting to public")
            redirect_url = 'http://localhost:8000/au/u/users/login'
        
        return Response(data={'data': serializer.data, 'login url': redirect_url})
