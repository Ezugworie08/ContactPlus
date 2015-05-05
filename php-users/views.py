from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from users.models import ContactOwner
from users.serializers import LoginRegisterSerializer


class RegisterContactOwner(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        owner = serializer.create(**serializer.validated_data)
        if owner:
            return Response(status=status.HTTP_201_CREATED)
        return Response("Sorry Bro!", status=status.HTTP_400_BAD_REQUEST)


class LoginContactOwner(APIView):

    # TODO: Write an `AllowRegistered` permission.
    # I know it will lead to redundant code but `AllowAny` for `login` operation sounds weird.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        owner = ContactOwner.objects.get(email=serializer.validated_data['email'])
        if owner.check_password(serializer.validated_data['password']):
            owner.login()
            return Response(owner.token, status=status.HTTP_201_CREATED)
        return Response("You've made a mess, Try again", status=status.HTTP_400_BAD_REQUEST)


class LogoutContactOwner(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        request.user.logout()
        return Response(status=status.HTTP_204_NO_CONTENT)






