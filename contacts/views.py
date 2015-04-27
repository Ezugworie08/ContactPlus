__author__ = 'Ikechukwu'

# My attempt at FAT Serializers and THIN Views

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework import generics


# Views rewritten using built-in generic views

class CreateListContact(generics.ListCreateAPIView):

    model = Contact
    serializer_class = ContactSerializer

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        return super(CreateListContact, self).post(self, request)


class RetrieveUpdateDeleteContact(generics.RetrieveUpdateDestroyAPIView):

    model = Contact
    serializer_class = ContactSerializer

    def put(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        return super(RetrieveUpdateDeleteContact, self).put(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        return super(RetrieveUpdateDeleteContact, self).patch(self, request, *args, **kwargs)

