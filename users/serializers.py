__author__ = 'Ikechukwu'
from django.core.exceptions import ValidationError

from rest_framework import serializers

from users.models import ContactOwner


def refactored_create(validated_object):
    new_owner = ContactOwner(
        email=validated_object['email'],
    )
    new_owner.set_password(validated_object['password'])
    new_owner.save()
    return new_owner


class LoginRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactOwner
        fields = ('email', 'password')
        # You might have to take this `write-only` restriction out.
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return refactored_create(validated_data)


# TODO: Ask Chris what he thinks.
class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, style={'input_type': 'password'})

    # TODO: Chris, what do you think about password verification?
    # password1 = serializers.CharField(min_length=8, style={'input_type': 'password'})
    # password2 = serializers.CharField(min_length=8, style={'input_type': 'password'})
    # password = serializers.SerializerMethodField()
    #
    # def get_password(self, obj):
    #     password1 = obj.validated_data.get('password1')
    #     password2 = obj.validated_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError('Passwords don\'t match')
    #     return password2

    def create(self, validated_data):
        return refactored_create(validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        if validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()