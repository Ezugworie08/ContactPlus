__author__ = 'Ikechukwu'

from rest_framework import serializers
from contacts.models import Contact
from django.contrib.auth.models import User
from localflavor.us.us_states import STATE_CHOICES


class ContactSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'aka', 'mobile',
                  'email', 'address', 'city', 'state', 'zip', 'avatar',)

    # def save(self, **kwargs):
    #     new_contact = self.model.objects.create(
    #         owner=kwargs['owner'],
    #         address=self.validated_data['address'],
    #
    #     )
    #     self.instance = new_contact
    #     return self.instance

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)
        read_only_fields = ('username', 'email',)