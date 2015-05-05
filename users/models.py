
import uuid
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
# Create your models here.


class ContactOwnerManager(BaseUserManager):

    def create_user(self, email, password):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        # TODO: ASK CHRIS which one is right.
        # user.is_staff = True
        user.save(using=self._db)
        return user


def gen_token():
    return str(uuid.uuid4())


class ContactOwner(PermissionsMixin, AbstractBaseUser):

    email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
    token = models.CharField(max_length=36, default=gen_token)

    USERNAME_FIELD = 'email'

    objects = ContactOwnerManager()

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.email

    def __str__(self):
        return "{0}: {1} {2}".format(self.email, self.username)

    def login(self):
        self.token = gen_token()
        self.last_login = now()
        self.save()

    def logout(self):
        self.token = ""
        self.save()