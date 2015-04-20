__author__ = 'Ikechukwu'

# My attempt at FAT Serializers and THIN Views

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class CreateListContact(APIView):

    def get(self, request):
        contacts = Contact.objects.filter(owner=request.user)
        result = ContactSerializer(contacts, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

    def post(self, request):
        incoming = ContactSerializer(data=request.data)
        if not incoming.is_valid():
            return Response(incoming.errors, status=status.HTTP_400_BAD_REQUEST)
        new_contact = incoming.create(owner=request.user)
        outgoing = ContactSerializer(instance=new_contact)
        return Response(outgoing.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeleteContact(APIView):

    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        result = ContactSerializer(instance=contact)
        return Response(result.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        This should work for PATCH too.
        :param request:
        :param pk:
        :return:
        """
        contact = Contact.objects.get(pk=pk)
        incoming = ContactSerializer(data=request.data)
        if not incoming.is_valid():
            return Response(incoming.errors, status=status.HTTP_400_BAD_REQUEST)
        updated_contact = incoming.update(instance=contact, validated_data=incoming.validated_data,
                                          owner=request.user)
        result = ContactSerializer(instance=updated_contact)
        return Response(result.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)