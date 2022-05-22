from rest_framework.viewsets import ModelViewSet
from contacts.models import Contact
from contacts.api.serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer