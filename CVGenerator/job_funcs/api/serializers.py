from rest_framework.serializers import ModelSerializer
from job_funcs.models import JobFunc


class JobFuncSerializer(ModelSerializer):
    class Meta:
        model = JobFunc
        fields = ['func']