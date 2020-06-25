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

from .models import Conducteur, Mission, Vehicule, Marque, Modele
from .serializers import *
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class MarqueList(APIView):
    """
    List all marques,Create new marque
    """

    def get(self, request, format=None):
        marque = Marque.objects.all()
        serializer = MarqueSerializer(marque, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=MarqueSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarqueDetail(APIView):
    """
    Retrieve, update or delete a Marque instance.
    """

    def get_object(self, pk):
        try:
            marque = Marque.objects.get(pk=pk)
            return marque
        except Marque.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        marque = self.get_object(pk)
        serializer = MarqueSerializer(marque)
        return Response(serializer.data)


class ModeleList(APIView):
    """
    List all Modeles,Create new Modele
    """


    def get(self, request, format=None):
        modele = Modele.objects.all()
        serializer = ModeleReadSerializer(modele, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=ModeleWriteSerializer(data=request.data)
        if serializer.is_valid():
          modele = serializer.save()
          serializer=ModeleReadSerializer(modele)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModeleDetail(APIView):
    """
    Retrieve, update or delete a Modele instance.
    """

    def get_object(self, pk):
        try:
            modele = Modele.objects.get(pk=pk)
            return modele
        except Modele.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        modele = self.get_object(pk)
        serializer = ModeleReadSerializer(modele)
        return Response(serializer.data)


class VehiculeList(APIView):
    """
    List all vehicules,Create new vehicule
    """

    #The request is authenticated
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        #CentralUser get all vehicules
        filter = {}
        #RegionalUser get vehicules of his region
        if request.user.user_type == 2:
            filter['region'] = request.user.region
        #OperationnelUser get vehicules of his region and his unite
        if request.user.user_type == 1:
            filter['region'] = request.user.region
            filter['unite'] = request.user.unite

        vehicules = Vehicule.objects.filter(**filter)
        serializer = VehiculeReadSerializer(vehicules, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data.copy()
        data['region'] = request.user.region
        data['unite'] = request.user.unite
        serializer=VehiculeWriteSerializer(data=data)
        if serializer.is_valid():
          vehicule = serializer.save()
          serializer=VehiculeReadSerializer(vehicule)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehiculeDetail(APIView):
    """
    Retrieve, update or delete a vehicule instance.
    """
    #The request is authenticated
    permission_classes = [IsAuthenticated]

    def get_object(request,self, pk):
        try:
            #CentralUser get all vehicules
            filter = {}
            #RegionalUser get vehicules of his region
            if request.user.user_type == 2:
                filter['region'] = request.user.region
            #OperationnelUser get vehicules of his region and his unite
            if request.user.user_type == 1:
                filter['region'] = request.user.region
                filter['unite'] = request.user.unite
            vehicule = Vehicule.objects.get(pk=pk,**filter)
            return vehicule
        except Vehicule.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vehicule = self.get_object(request,pk)
        serializer = VehiculeReadSerializer(vehicule)
        return Response(serializer.data)

class ConducteurList(APIView):
    """
    List all conducteurs,Create new conducteur
    """
    #The request is authenticated
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        #CentralUser get all vehicules
        filter = {}
        #RegionalUser get conducteurs of his region
        if request.user.user_type == 2:
            filter['region'] = request.user.region
        #OperationnelUser get conducteurs of his region and his unite
        if request.user.user_type == 1:
            filter['region'] = request.user.region
            filter['unite'] = request.user.unite

        conducteurs = Conducteur.objects.filter(**filter)
        serializer = ConducteurSerializer(conducteurs, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data.copy()
        data['region'] = request.user.region
        data['unite'] = request.user.unite
        serializer=ConducteurSerializer(data=data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConducteurDetail(APIView):
    """
    Retrieve, update or delete a conducteur instance.
    """
    #The request is authenticated
    permission_classes = [IsAuthenticated]
    def get_object(self,request,pk):
        try:
            #CentralUser get all vehicules
            filter = {}
            #RegionalUser get vehicules of his region
            if request.user.user_type == 2:
                filter['region'] = request.user.region
            #OperationnelUser get vehicules of his region and his unite
            if request.user.user_type == 1:
                filter['region'] = request.user.region
                filter['unite'] = request.user.unite
            conducteur = Conducteur.objects.get(pk=pk,**filter)
            return conducteur
        except Conducteur.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        conducteur = self.get_object(request,pk)
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
        serializer=MissionWriteSerializer(data)
        # vehicule = Vehicule.objects.get(pk=data['vehicule'])
        # conducteur = Vehicule.objects.get(pk=data['conducteur'])
        # if not (vehicule.region == request.user.region and vehicule.unite == request.user.unite and conducteur.region == request.user.region and conducteur.unite == request.user.unite):
        #     return Response({"error": "vehicule ou conducteur n'ont pas la méme region/unite que l'utilisateur"}, status=status.HTTP_400_BAD_REQUEST)
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
