__author__ = 'Ikechukwu'

# My attempt at FAT Serializers and THIN Views

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from contacts.permissions import IsOwner

# Views rewritten using built-in generic views


class CreateListContact(generics.ListCreateAPIView):

    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        return super(CreateListContact, self).post(self, request, *args, **kwargs)


class RetrieveUpdateDeleteContact(generics.RetrieveUpdateDestroyAPIView):

    model = Contact
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def put(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        return super(RetrieveUpdateDeleteContact, self).put(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        return super(RetrieveUpdateDeleteContact, self).patch(self, request, *args, **kwargs)

