# projects/serializers.py
from rest_framework import serializers
from .models import Project 

class ProjectSerializer(serializers.ModelSerializer): # <--- Cambiado a ProjectSerializer
    class Meta:
        model = Project
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'f_creacion')
        read_only_fields = ('f_creacion', )