from rest_framework.viewsets import ModelViewSet
from job_funcs.models import JobFunc
from job_funcs.api.serializers import JobFuncSerializer


class JobFuncViewSet(ModelViewSet):
    queryset = JobFunc.objects.all()
    serializer_class = JobFuncSerializer
