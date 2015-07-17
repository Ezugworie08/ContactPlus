__author__ = 'Ikechukwu'

from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'owner', 'first_name', 'last_name', 'aka', 'mobile',
                  'email', 'address', 'city', 'state', 'zip_code', 'avatar',)
        # extra_kwargs = {'id': {'read_only': True}}

    # def create(self, validated_data, **kwargs):
    #     new_instance = Contact(
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         aka=validated_data['aka'],
    #         mobile=validated_data['mobile'],
    #         email=validated_data['email'],
    #         address=validated_data['address'],
    #         city=validated_data['city'],
    #         state=validated_data['state'],
    #         zip_code=validated_data['zip_code'],
    #         avatar=validated_data['avatar'],
    #         owner=validated_data['owner'],
    #         # owner=kwargs.pop('owner')
    #     )
    #     return new_instance
    #
    # def update(self, instance, validated_data, **kwargs):
    #     instance.first_name = validated_data.get('first_name', instance.first_name),
    #     instance.last_name = validated_data.get('last_name', instance.last_name),
    #     instance.aka = validated_data.get('aka', instance.aka),
    #     instance.mobile = validated_data.get('mobile', instance.mobile),
    #     instance.email = validated_data.get('email', instance.email),
    #     instance.address = validated_data.get('address', instance.address),
    #     instance.city = validated_data.get('city', instance.city),
    #     instance.state = validated_data.get('state', instance.state),
    #     instance.zip_code = validated_data.get('zip_code', instance.zip_code),
    #     instance.avatar = validated_data.get('avatar', instance.avatar),
    #     # instance.owner = kwargs.pop('owner')
    #     instance.owner = validated_data.get('owner', instance.owner),
    #     instance.save()
    #     return instance
