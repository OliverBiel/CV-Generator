from rest_framework.viewsets import ModelViewSet
from myprofile.models import MyProfile
from myprofile.api.serializers import MyProfileSerializer


class MyProfileViewSet(ModelViewSet):
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileSerializer