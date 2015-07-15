__author__ = 'Ikechukwu'
# from django.core.exceptions import ValidationError

from rest_framework import serializers

from users.models import ContactOwner


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactOwner
        fields = ('email', 'password', 'token')
        # You might have to take this `write-only` restriction out.
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        new_owner = ContactOwner(email=validated_data['email'],)
        new_owner.set_password(validated_data['password'])
        new_owner.save()
        return new_owner

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        if validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=False, style={'input_type': 'password'})
    token = serializers.CharField(required=False, default='')

    def create(self, validated_data):
        new_owner = ContactOwner(email=validated_data['email'],)
        new_owner.set_password(raw_password=validated_data['password'])
        new_owner.save()
        return new_owner

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        if validated_data['password']:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
