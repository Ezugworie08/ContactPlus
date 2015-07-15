
import uuid
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
# Create your models here.


class ContactOwnerManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


def gen_token():
    return str(uuid.uuid4())


class ContactOwner(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
    token = models.CharField(max_length=36, default="")

    USERNAME_FIELD = 'email'

    objects = ContactOwnerManager()

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def login(self):
        self.token = gen_token()
        self.last_login = now()
        self.save()

    def logout(self):
        self.token = ""
        self.save()
