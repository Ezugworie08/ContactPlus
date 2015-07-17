"""
    This is the basic model of a users contact.
"""

from django.db import models
from users.models import ContactOwner

from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USZipCodeField, PhoneNumberField

# TODO: Put a gender choices and add a gender field later.
# TODO: Add a search end point


class Contact(models.Model):

    owner = models.ForeignKey(ContactOwner, related_name='contacts')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=35)
    aka = models.CharField(max_length=40, blank=True, default="")
    mobile = PhoneNumberField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=220)
    city = models.CharField(max_length=50)  # get django city extensions
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip_code = USZipCodeField(blank=True, default="")
    avatar = models.URLField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return """
            My name is {0} {1}. Shoot me an Email at {2}
            """.format(self.first_name, self.last_name, self.email)
