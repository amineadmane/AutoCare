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
from .permissions import IsAuthenticatedOrReadOnly
from .models import Piece, Guide_constructure, Guide_personnel
from .serializers import *
# Create your views here.

class PieceList(APIView):
    """
    List all Pieces,Create new Piece
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):

        #filtrage par modele 
        filter = {}

        if 'modele' in request.GET:
            filter['modele'] = request.GET['modele']


        pieces = Piece.objects.filter(**filter)
        serializer = PieceReadSerializer(pieces, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=PieceWriteSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PieceDetail(APIView):
    """
    Retrieve, update or delete a Piece instance.
    """
    #The request is authenticated, or is a read-only request.
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            piece = Piece.objects.get(pk=pk)
            return piece
        except Piece.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        piece = self.get_object(pk)
        serializer = PieceReadSerializer(piece)
        return Response(serializer.data)

    def delete(self,request,pk):
        piece=self.get_object(pk)
        piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




        ###########################################################################
#############################  Guide_constructure  #############################################


class Guide_constructureList(APIView):
    """
    List all Guide_constructure,Create new Guide_constructure
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):

        #filtrage par piece 
        filter = {}

        if 'piece' in request.GET:
            filter['piece'] = request.GET['piece']


        gcs = Guide_constructure.objects.filter(**filter)
        serializer = Guide_constructureReadSerializer(gcs, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=Guide_constructureWriteSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Guide_constructureDetail(APIView):
    """
    Retrieve, update or delete a Guide_constructure instance.
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            gc = Guide_constructure.objects.get(pk=pk)
            return gc
        except Guide_constructure.DoesNotExist:
            raise Http404 

    def get(self, request, pk, format=None):
        gc = self.get_object(pk)
        serializer = Guide_constructureReadSerializer(gc)
        return Response(serializer.data)




        ###########################################################################
#############################  Guide_personnel  #############################################


class Guide_personnelList(APIView):
    """
    List all Guide_personnel,Create new Guide_personnel
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):

        #filtrage par piece 
        filter = {}

        if 'piece' in request.GET:
            filter['piece'] = request.GET['piece']


        gps = Guide_personnel.objects.filter(**filter)
        serializer = Guide_personnelReadSerializer(gps, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=Guide_personnelWriteSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Guide_personnelDetail(APIView):
    """
    Retrieve, update or delete a Guide_constructure instance.
    """
    #The request is authenticated, or is a read-only request.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            gp = Guide_personnel.objects.get(pk=pk)
            return gp
        except Guide_personnel.DoesNotExist:
            raise Http404 

    def get(self, request, pk, format=None):
        gp = self.get_object(pk)
        serializer = Guide_personnelReadSerializer(gp)
        return Response(serializer.data)

