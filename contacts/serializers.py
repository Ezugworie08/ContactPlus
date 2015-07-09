__author__ = 'Ikechukwu'

from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'owner', 'first_name', 'last_name', 'aka', 'mobile',
                  'email', 'address', 'city', 'state', 'zip_code', 'avatar',)

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
            zip_code=self.validated_data['zip_code'],
            avatar=self.validated_data['avatar'],
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
        instance.zip_code = validated_data.get('zip_code', instance.zip_code),
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.owner = kwargs.pop('owner')
        instance.save()
        return instance
