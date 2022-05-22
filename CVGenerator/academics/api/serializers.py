from rest_framework.serializers import ModelSerializer
from academics.models import Academic


class AcademicSerializer(ModelSerializer):
    class Meta:
        model = Academic
        fields = ['name', 'institution', 'start_date', 'end_date']