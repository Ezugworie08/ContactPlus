# from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from contacts.models import Contact
from contacts.old_serializers import ContactSerializer
# from contacts.serializers import UserSerializer


# Create your views here.
# This is written assuming that the user is authenticated and logged-in
# Create from scratch and leave on github


class ContactListCreate(APIView):

    def get(self, request):
        contacts = Contact.objects.filter(user=request.user)
        result = ContactSerializer(contacts, many=True)
        return Response(result.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContactSerializer(request.data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # new_contact = Contact.objects.create(owner=request.user, **serializer.validated_data)
        # result = ContactSerializer(new_contact)
        # return Response(result.data, status=status.HTTP_201_CREATED)

        if serializer.is_valid():
            # I am hoping `save()` knows that the owner argument is part of the data to be saved.
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

class ContactRetrieveUpdateDelete(APIView):

    def get_object(self, pk):
        return Contact.objects.get(pk=pk)

    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # updated_contact = Contact.objects.create(owner=request.user, **serializer.validated_data)
        # result = ContactSerializer(updated_contact)
        # return Response(result.data, status=status.HTTP_200_OK)

        if serializer.is_valid():
            # I am hoping `save()` knows that the owner argument is part of the data to be saved.
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data, partial=True)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # updated_contact = Contact.objects.create(owner=request.user, **serializer.validated_data)
        # result = ContactSerializer(updated_contact)
        # return Response(result.data, status=status.HTTP_200_OK)

        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ContactListCreate(APIView):
#     """
#     List all the contacts as well as create a Contact
#     """
#     def get(self, request, format=None):
#         contacts = Contact.objects.filter(owner=request.user)
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         contact = ContactSerializer(data=request.data)
#         if contact.is_valid():
#             # Since the owner field isn't being serialized, I am adding it upon save.
#             # I don't if this works or not.
#             contact.save(owner=request.user)
#             return Response(contact.data, status=status.HTTP_201_CREATED)
#         return Response(contact.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ContactDetailRetrieveUpdateDelete(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(pk=pk)
#         except Contact.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact, data=request.data)
#         if serializer.is_valid():
#             # Since the owner field isn't being serialized, I am adding it upon save.
#             # I don't if this works or not.
#             serializer.save(owner=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk, format=None):
#         contact = self.get_object(pk)
#         serializer = ContactSerializer(contact, data=request.data, partial=True)
#         if serializer.is_valid():
#             # Since the owner field isn't being serialized, I am adding it upon save.
#             # I don't if this works or not.
#             serializer.save(owner=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         contact = self.get_object(pk)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    pass


class UserDetail(APIView):
    pass