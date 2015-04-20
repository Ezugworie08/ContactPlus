"""
    This is the basic model of a users contact.
"""
from django.db import models
from django.contrib.auth.models import User
from localflavor.us.us_states import STATE_CHOICES

# Create your models here.
# Update fields to use the new django extensions


class Contact(models.Model):
    owner = models.ForeignKey('User', related_name='contacts')  # Using Django's bundled user mgt system.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=35)
    aka = models.CharField(max_length=40, blank=True, default="")
    mobile = models.CharField(max_length=10)  # get django_phone number extension
    email = models.EmailField()
    address = models.CharField(max_length=220)
    city = models.CharField(max_length=50)  # get django city extensions
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.CharField(max_length=5)
    avatar = models.URLField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "I am {0} {1}".format(self.first_name, self.last_name)