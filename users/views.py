import json
import sys

import requests
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.http import (Http404, HttpResponseBadRequest,
                         HttpResponseForbidden, JsonResponse)

from rest_framework import parsers, renderers, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import *
from .permissions import AdminOnly, IsNotAuthenticated, OwnerOnly
from .serializers import SignUpSerializer, UserSerializer



class AdminSign(APIView):
    ''' Admin user create accounts '''

    #permission to admins only
    permission_classes = [IsAuthenticated, AdminOnly]

    def post(self, request):

        #FOR DEBUG
        print(request.headers)
        sys.stdout.flush()
        ###############

        response = {}
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user).key
            user = UserSerializer(user)
            response = user.data.copy()
            response.update({'token': token})
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersList(APIView):
    """
    List all users , filter with user_type
    """
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        #Parse request filters
        filters = {}
        if "user_type" in request.GET:
            if request.GET["user_type"] == "admin":
                filters["user_type"] = 0
            elif request.GET["user_type"] == "operationnel":
                filters["user_type"] = 1
            elif request.GET["user_type"] == "regional":
                filters["user_type"] = 2
            elif request.GET["user_type"] == "central":
                filters["user_type"] = 3


        users = User.objects.filter(**filters)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = [OwnerOnly]

    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            #GET USER DETAIL CAN BE DONE BY EVERYONE
            if self.request.method != "GET":
                self.check_object_permissions(self.request, user)
            return user
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)










#Login Rest Framework
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data.copy()
        data.update({'token': token.key})
        return Response(data)
