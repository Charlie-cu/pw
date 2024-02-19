from .models import Admin,Examen,Docente,Estudiante,Subject
from rest_framework import serializers

class Examen_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Examen
        fields="__all__"

class Admin_Serializer(serializers.ModelSerializer):
     class Meta:
        model=Admin
        fields=
        
class Docente_Serializer(serializers.ModelSerializer):
     class Meta:
        model=Docente
        fields=
        
class Estudiante_Serializer(serializers.ModelSerializer):
     class Meta:
        model=Estudiante
        fields=
        
class Subject_Serializer(serializers.ModelSerializer):
     class Meta:
        model=Subject
        fields="__all__"
        
        