from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from braces import views

from users.models import ContactOwner
from users.serializers import RegisterSerializer, LoginSerializer


class RegisterContactOwner(views.AnonymousRequiredMixin, APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # # For the fact that `raise_exception` is set to `True`, It means that if
        # # `serializer.is_valid()` encounters any errors, the program will stop
        # # There's no need for the `if` statement below.
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        owner = serializer.create(serializer.validated_data)
        owner.login()
        return Response(owner.token, status=status.HTTP_201_CREATED)


class UpdateContactOwner(views.LoginRequiredMixin, APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        serializer = RegisterSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        owner = serializer.update(serializer.validated_data)
        if owner:
            # Either the password or email has been updated, so we need to reset token
            owner.login()
            return Response(owner.token, status=status.HTTP_201_CREATED)
            # I honestly don't know what the right status code is
        return Response("Sorry folks! Try again", status=status.HTTP_400_BAD_REQUEST)


class LoginContactOwner(views.AnonymousRequiredMixin, APIView):

    # TODO: Write an `AllowRegistered` permission.
    # I know it will lead to redundant code but `AllowAny` for `login` operation sounds weird.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        owner = ContactOwner.objects.get(email=serializer.validated_data['email'])
        if owner.check_password(serializer.validated_data['password']):
            owner.login()
            return Response(owner.token, status=status.HTTP_201_CREATED)
        return Response("You've made a mess, Try again", status=status.HTTP_400_BAD_REQUEST)


class LogoutContactOwner(views.LoginRequiredMixin, APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        print(request)
        request.user.logout()
        return Response(status=status.HTTP_204_NO_CONTENT)
