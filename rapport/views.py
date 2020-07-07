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
from mission.models import Conducteur, Vehicule
from .models import RapportSignalProbleme, RapportSignalChauffeur, RapportSignalSinistre
from .serializers import *
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class RapportSignalProblemeList(APIView):
    """
    List all RapportSignalProbleme  ,Create new RapportSignalProbleme
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        rapports = RapportSignalProbleme.objects.all()
        serializer = RapportSignalProbleme_ReadSerializer(rapports, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data.copy()
        data['redacteur'] = request.user.id
        serializer=RapportSignalProbleme_WriteSerializer(data=data)
        if serializer.is_valid():
          rapport = serializer.save()
          serializer = RapportSignalProbleme_ReadSerializer(rapport)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RapportSignalProblemeDetail(APIView):
    """
    Retrieve, update or delete a RapportSignalProbleme instance.
    """

    def get_object(self, pk):
        try:
            rapport = RapportSignalProbleme.objects.get(pk=pk)
            return rapport
        except RapportSignalProbleme.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rapport = self.get_object(pk)
        serializer = RapportSignalProbleme_ReadSerializer(rapport)
        return Response(serializer.data)


class ValidateRapportSignalProbleme(APIView):

    def get_object(self, pk):
        try:
            rapport = RapportSignalProbleme.objects.get(pk=pk)
            return rapport
        except RapportSignalProbleme.DoesNotExist:
            raise Http404


    def patch(self, request, pk, format=None):
        data = {}
        rapport = self.get_object(pk)
        data['confirmed'] = True
        serializer = RapportSignalProbleme_WriteSerializer(rapport, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InValidateRapportSignalProbleme(APIView):

    def get_object(self, pk):
        try:
            rapport = RapportSignalProbleme.objects.get(pk=pk)
            return rapport
        except RapportSignalProbleme.DoesNotExist:
            raise Http404


    def patch(self, request, pk, format=None):
        data = {}
        rapport = self.get_object(pk)
        data['confirmed'] = False
        serializer = RapportSignalProbleme_WriteSerializer(rapport, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RapportSignalChauffeurList(APIView):
    """
    List all RapportSignalChauffeur,Create new RapportSignalChauffeur
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        rapports = RapportSignalChauffeur.objects.all()
        serializer = RapportSignalChauffeur_ReadSerializer(rapports, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data.copy()
        data['redacteur'] = request.user.id
        serializer=RapportSignalChauffeur_WriteSerializer(data=data)
        if serializer.is_valid():
          rapport = serializer.save()
          serializer=RapportSignalChauffeur_ReadSerializer(rapport)
          #reduce score of "chauffeur" depends on the "gravite"
          if data['gravite'] == "FAIBLE":
              Conducteur.objects.filter(pk=data['conducteur']).update(score=F('score') - 5)
          elif data['gravite'] == "MOYEN":
              Conducteur.objects.filter(pk=data['conducteur']).update(score=F('score') - 10)
          elif data['gravite'] == "FORT":
              Conducteur.objects.filter(pk=data['conducteur']).update(score=F('score') - 20)
          elif data['gravite'] == "CRITIQUE":
              Conducteur.objects.filter(pk=data['conducteur']).update(score=F('score') - 30)

          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RapportSignalChauffeurDetail(APIView):
    """
    Retrieve, update or delete a RapportSignalChauffeur instance.
    """

    def get_object(self, pk):
        try:
            rapport = RapportSignalChauffeur.objects.get(pk=pk)
            return rapport
        except RapportSignalChauffeur.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rapport = self.get_object(pk)
        serializer = RapportSignalChauffeur_ReadSerializer(rapport)
        return Response(serializer.data)







class RapportSignalSinistreList(APIView):
    """
    List all RapportSignalSinistre,Create new RapportSignalSinistre
    """

    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]
    

    def get(self, request, format=None):
        rapports = RapportSignalSinistre.objects.all()
        serializer = RapportSignalSinistre_ReadSerializer(rapports, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data.copy()
        data['redacteur'] = request.user.id
        serializer=RapportSignalSinistre_WriteSerializer(data=data)
        if serializer.is_valid():
          rapport = serializer.save()
          serializer = RapportSignalSinistre_ReadSerializer(rapport)
        
          #critique ==> vehicule etat == hds
          if data['gravite'] == "CRITIQUE":
              Vehicule.objects.filter(pk=data['vehicule']).update(etat="HDS")

          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RapportSignalSinistreDetail(APIView):
    """
    Retrieve, update or delete a RapportSignalSinistre instance.
    """

    def get_object(self, pk):
        try:
            rapport = RapportSignalSinistre.objects.get(pk=pk)
            return rapport
        except RapportSignalSinistre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rapport = self.get_object(pk)
        serializer = RapportSignalSinistre_ReadSerializer(rapport)
        return Response(serializer.data)


