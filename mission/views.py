import datetime
import sys

import requests
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import F, Max, Sum
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Conducteur, Mission, Vehicule
from .serializers import *
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class VehiculeList(APIView):
    """
    List all vehicules,Create new vehicule
    """

    def get(self, request, format=None):
        vehicules = Vehicule.objects.all()
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=VehiculeSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehiculeDetail(APIView):
    """
    Retrieve, update or delete a vehicule instance.
    """

    def get_object(self, pk):
        try:
            vehicule = Vehicule.objects.get(pk=pk)
            return vehicule
        except Vehicule.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vehicule = self.get_object(pk)
        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)



class ConducteurList(APIView):
    """
    List all conducteurs,Create new conducteur
    """

    def get(self, request, format=None):
        conducteurs = Conducteur.objects.all()
        serializer = ConducteurSerializer(conducteurs, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=ConducteurSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConducteurDetail(APIView):
    """
    Retrieve, update or delete a conducteur instance.
    """

    def get_object(self, pk):
        try:
            conducteur = Conducteur.objects.get(pk=pk)
            return conducteur
        except Conducteur.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        conducteur = self.get_object(pk)
        serializer = ConducteurSerializer(conducteur)
        return Response(serializer.data)



class MissionList(APIView):
    """
    List all Missions,Create new Mission
    """
    
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        mission = Mission.objects.all()
        serializer = MissionReadSerializer(mission, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data.copy()
        data['redacteur'] = request.user.id
        serializer=MissionWriteSerializer(data=data)
        if serializer.is_valid():
          mission = serializer.save()
          serializer=MissionReadSerializer(mission)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MissionDetail(APIView):
    """
    Retrieve, update or delete a Mission instance.
    """

    def get_object(self, pk):
        try:
            mission = Mission.objects.get(pk=pk)
            return mission
        except Mission.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mission = self.get_object(pk)
        serializer = MissionReadSerializer(mission)
        return Response(serializer.data)
