__author__ = 'Ikechukwu'

from rest_framework import serializers
from .models import Contact
from django.contrib.auth.models import User
# from localflavor.us.us_states import STATE_CHOICES


class ContactSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'aka', 'mobile',
                  'email', 'address', 'city', 'state', 'zip', 'avatar',)

    # I found that the Base serializer in DRF does not implement
    # `create()`, and `update()` which requires and `instance`
    # argument just as you taught me.
    # The defined `save()` calls the `create` and `update` operations
    # if their respective requirements are met.

    def save(self, **kwargs):
        new_instance = self.model.objects.create(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            aka=self.validated_data['aka'],
            mobile=self.validated_data['mobile'],
            email=self.validated_data['email'],
            address=self.validated_data['address'],
            city=self.validated_data['city'],
            state=self.validated_data['state'],
            zip=self.validated_data['zip'],
            avatar=self.validated_data['avatar'],
            # This mandates that the `owner` is passed in as part
            # keyword args and as thus `owner=request.user`
            # Since it is a Models.ForeignKeyField, which means it must not be empty,
            # I don't know what default value to provide for `.pop()`
            owner=kwargs.pop('owner')
        )
        self.instance = new_instance
        return self.instance

    def create(self, **kwargs):
        return self.save(**kwargs)

    def update(self, instance, validated_data, **kwargs):
        instance.first_name = validated_data.get('first_name', instance.first_name),
        instance.last_name = validated_data.get('last_name', instance.last_name),
        instance.aka = validated_data.get('aka', instance.aka),
        instance.mobile = validated_data.get('mobile', instance.mobile),
        instance.email = validated_data.get('email', instance.email),
        instance.address = validated_data.get('address', instance.address),
        instance.city = validated_data.get('city', instance.city),
        instance.state = validated_data.get('state', instance.state),
        instance.zip = validated_data.get('zip', instance.zip),
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.owner = kwargs.pop('owner')
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)
        read_only_fields = ('username', 'email',)