from rest_framework.serializers import ModelSerializer
from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    model = Contact
    fields = ['name', 'logo', 'info']
