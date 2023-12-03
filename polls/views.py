from rest_framework import viewsets, permissions
from .models import Skill, Project, Correo
from .serializers import SkillSerializer, ProjectSerializer, CorreoSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SkillSerializer
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    
class CorreoViewSet(viewsets.ModelViewSet):
    queryset = Correo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CorreoSerializer