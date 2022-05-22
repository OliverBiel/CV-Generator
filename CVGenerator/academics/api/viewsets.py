from rest_framework.viewsets import ModelViewSet
from academics.models import Academic
from academics.api.serializers import AcademicSerializer


class AcademicViewSet(ModelViewSet):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer