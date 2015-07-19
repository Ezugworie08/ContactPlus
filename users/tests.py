from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from users.mixins import LoginUserMixin
from contacts.mixins import TestUserMixin

# user/register
# user/login
# user/logout


class RegisterUserTest(APITestCase):

    EMAIL = 'rapast@yahoo.com'
    PASSWORD = 'aVadacadavRa02'

    def test_register_user(self):
        url = reverse('users:register')
        data = {
            'email': self.EMAIL,
            'password': self.PASSWORD,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data, data)

    def test_register_user_without_email(self):
        url = reverse('users:register')
        data = {
            'password': self.PASSWORD,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data)
        self.assertIn('This field is required.', response.data['email'])

    def test_register_user_without_password(self):
        url = reverse('users:register')
        data = {
            'email': self.EMAIL,
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data)
        self.assertIn('This field is required.', response.data['password'])


class LoginUserTest(LoginUserMixin, APITestCase):

    def test_login_user(self):
        url = reverse('users:login')
        data = {
            'email': self.EMAIL,
            'password': self.PASSWORD
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data)

    def test_login_user_without_email(self):
        url = reverse('users:login')
        data = {
            'password': self.PASSWORD
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data)
        self.assertIn('This field is required.', response.data['email'])

    def test_login_user_without_password(self):
        url = reverse('users:login')
        data = {
            'email': self.EMAIL
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data)
        self.assertIn('This field is required.', response.data['password'])


class LogoutUserTest(TestUserMixin, APITestCase):

    def test_logout_authenticated_user(self):
        url = reverse('users:logout')
        response = self.client.delete(url, **self.auth)
        self.assertEqual(response.data, None)
        self.assertTrue(response)
        print(response.data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logout_not_authenticated_user(self):
        url = reverse('users:logout')
        response = self.client.delete(url)
        self.assertNotEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(response.data)
        self.assertIn('Authentication credentials were not provided.', response.data['detail'])

