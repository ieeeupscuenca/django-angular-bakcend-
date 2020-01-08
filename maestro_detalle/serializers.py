from rest_framework import serializers
from maestro_detalle.models import Persona,Direccion

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('id','codigo','callePrincipal','calleSecundaria','numeroCasa')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','codigo','nombre','apellido','fechaNacimiento','edad','sexo','direccion')