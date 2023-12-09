from rest_framework import serializers
from .models import Skill, Project, Correo

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    skills_project = SkillSerializer(many=True, source='skills', read_only=True)
    class Meta:
        model = Project
        fields = ('id','nombre','descripcion','foto','skills_project','url')

class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = '__all__'