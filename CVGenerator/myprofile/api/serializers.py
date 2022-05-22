from rest_framework.serializers import ModelSerializer
from myprofile.models import MyProfile


class MyProfileSerializer(ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ['name', 'description']
