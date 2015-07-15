__author__ = 'Ikechukwu'

# My attempt at FAT Serializers and THIN Views

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from contacts.permissions import IsOwner
from contacts.filters import IsOwnerFilterBackend

# Views rewritten using built-in generic views


class ContactSearch(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # Ask Chris to help you figure out perms_map from
    # http://www.django-rest-framework.org/api-guide/filtering/#djangoobjectpermissionsfilter
    permission_classes = (IsAuthenticated, IsOwner)
    filter_backends = (IsOwnerFilterBackend, SearchFilter, OrderingFilter,)  # Unsure so ask Chris
    search_fields = (
        '^first_name', '^last_name', '=email', '=mobile',
        '=zip_code', '^aka', '=state', '=city',
    )
    ordering_fields = ('last_name', 'first_name', 'email', 'state', 'city', 'mobile')
    ordering = '__all__'
#   Ask chris if this needs a url


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
