from django.urls import path
from rest_framework import routers
from .views import SkillViewSet, ProjectViewSet, CorreoViewSet

router = routers.DefaultRouter()
router.register('api/skills', SkillViewSet)
router.register('api/projects', ProjectViewSet)
router.register('api/correos', CorreoViewSet)

urlpatterns = router.urls

app_name = 'polls'

