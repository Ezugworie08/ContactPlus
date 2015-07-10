# from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from users.mixins import TestUserMixin

# Create your tests here.
# To create a contact, the user has to be authenticated.
# So figure out how to do this authentication thing first,
# Write the user `tests` then go from there.
# Honestly, this whole `Token Auth business isn't crystal yet`

# Since your comprehension sucks, ask Chris what the Note around
# Forcing CSRF validation means in the Testing page of DRF API docs

# user/register
# user/login
# user/logout


class CreateUserTest(TestUserMixin, APITestCase):

    # Do not forget to test for a valid login here since `register` calls `login`

    def test_create_user(self):
        url = reverse('users:register')

        data = {
            'first_name': self.FIRST_NAME,
            'last_name': self.LAST_NAME,
            'email': self.EMAIL,
            'password': self.PASSWORD,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data)
        self.assertTrue(response.data['id'])
        self.assertTrue(response.data['token'])
        self.assertTrue(response.data['last_login'])
        self.assertEqual(response.data['email'], self.EMAIL)
        self.assertEqual(response.data['password'], self.PASSWORD)

    def test_create_user_without_email(self):

        url = reverse('users:register')

        data = {
            'first_name': self.FIRST_NAME,
            'last_name': self.LAST_NAME,
            'password': self.PASSWORD,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertTrue(response.errors), See comment below.
        self.assertTrue(response.data)
        # According to the docs, the error[s] come with a `detail`/`field name` key if it is a Validation error.
        self.assertIn('This field may not be blank.', response.data['email'])


class LoginUserTest(TestUserMixin, APITestCase):

    client = APIClient()

    def test_login_user(self):
        url = reverse('users:login')
