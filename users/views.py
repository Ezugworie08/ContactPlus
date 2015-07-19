from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from users.models import ContactOwner
from users.serializers import RegisterSerializer, LoginSerializer


class RegisterContactOwner(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        owner = serializer.create(serializer.validated_data)
        owner.login()
        return Response(owner.token, status=status.HTTP_201_CREATED)


class LoginContactOwner(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        owner = ContactOwner.objects.get(email=email)
        if owner.check_password(raw_password=password):
            owner.login()
            return Response(owner.token, status=status.HTTP_201_CREATED)
        return Response("invalid password", status=status.HTTP_401_UNAUTHORIZED)


class LogoutContactOwner(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        request.user.logout()
        return Response(status=status.HTTP_204_NO_CONTENT)
