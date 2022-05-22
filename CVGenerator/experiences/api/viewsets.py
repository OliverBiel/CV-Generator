from rest_framework.viewsets import ModelViewSet
from experiences.models import Experience
from experiences.api.serializers import ExperienceSerializer


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer