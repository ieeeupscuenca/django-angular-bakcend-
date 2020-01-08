from django.shortcuts import render

from rest_framework import generics

from maestro_detalle.models import Persona,Direccion
from maestro_detalle.serializers import PersonaSerializer,DireccionSerializer

class DireccionList(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class  DireccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class  PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
