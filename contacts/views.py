__author__ = 'Ikechukwu'

from rest_framework import generics, mixins, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from contacts.permissions import IsOwner
from contacts.filters import IsOwnerFilterBackend


class ContactSearch(generics.ListAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    filter_backends = (IsOwnerFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = (
        '^first_name', '^last_name', '=email', '=mobile',
        '=zip_code', '^aka', '=state', '=city',
    )
    ordering_fields = ('last_name', 'first_name', 'email', 'state', 'city', 'mobile')
    ordering = '__all__'


class CreateListContact(views.APIView):

    def get(self, request):
        contacts = Contact.objects.filter(owner=request.user)
        result = ContactSerializer(contacts, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        incoming = ContactSerializer(data=request.data)
        if not incoming.is_valid(raise_exception=True):
            return Response(incoming.errors, status=status.HTTP_400_BAD_REQUEST)
        new_contact = incoming.create(incoming.validated_data)
        outgoing = ContactSerializer(instance=new_contact)
        return Response(outgoing.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeleteContact(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):

    model = Contact
    serializer_class = ContactSerializer
    lookup_field = 'pk'
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def my_get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get(self, request, pk):
        contact = self.my_get_object(pk)
        result = ContactSerializer(contact)
        return Response(result.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        contact = self.my_get_object(pk)
        incoming = ContactSerializer(instance=contact, data=request.data, partial=True)
        if not incoming.is_valid(raise_exception=True):
            return Response(incoming.errors, status=status.HTTP_400_BAD_REQUEST)
        new_contact = incoming.save()
        outgoing = ContactSerializer(instance=new_contact)
        return Response(outgoing.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        contact = self.my_get_object(pk)
        incoming = ContactSerializer(instance=contact, data=request.data, partial=True)
        if not incoming.is_valid(raise_exception=True):
            return Response(incoming.errors, status=status.HTTP_400_BAD_REQUEST)
        new_contact = incoming.save()
        outgoing = ContactSerializer(instance=new_contact)
        return Response(outgoing.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        contact = self.my_get_object(pk)
        contact.delete()
        print("This shit ran like hell.")
        return Response(status=status.HTTP_204_NO_CONTENT)
