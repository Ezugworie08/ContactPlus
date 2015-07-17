from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from contacts.mixins import TestUserMixin #, TestContactMixin

# Create your tests here.
"""
Test these:
contact/:id GET
contact/:id PATCH, test for same as POST
contact/:id DELETE


To test for `listing contacts`, create 3 samples of dummy contact data,
define a creation model
"""


class CreateListContactTest(TestUserMixin, APITestCase):

    def test_create_contact(self):

        url = reverse('contacts:contact-create-list')
        data = {
            'first_name': "Rapast",
            'last_name': "Eme",
            'mobile': "+17898823654",
            'email': "zombie@zombie.com",
            'state': "AZ",
            'city': "jedi",
            'zip_code': "50578-4545",
            'address': "112 Edem Road, Ekwulobia",
        }
        self.client.credentials(**self.auth)
        response = self.client.post(url, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data)
        self.assertTrue(response.data['owner'])

    def test_create_multiple_get_all_contacts(self):
        url = reverse('contacts:contact-create-list')
        data = [
            {
                'first_name': "Tonto",
                'last_name': "Olof",
                'mobile': "+17898822254",
                'email': "bie@zombie.com",
                'state': "AZ",
                'city': "jedi",
                'zip_code': "50578-4545",
                'address': "113 Edem Road, Ekwulobia",
            },
            {
                'first_name': "Raik",
                'last_name': "DB",
                'mobile': "+15848823654",
                'email': "mie@zombie.com",
                'state': "AZ",
                'city': "jedi",
                'zip_code': "50578-4545",
                'address': "114 Edem Road, Ekwulobia",
            },
            {
                'first_name': "Yanki",
                'last_name': "Twizzy",
                'mobile': "+14898823654",
                'email': "zoe@zombie.com",
                'state': "AZ",
                'city': "jedi",
                'zip_code': "50578-4545",
                'address': "115 Edem Road, Ekwulobia",
            },
        ]
        self.client.credentials(**self.auth)
        for user in data:
            post_response = self.client.post(url, data=user, format='json')
            self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(post_response.data)
            self.assertTrue(post_response.data['owner'])
        get_response = self.client.get(url)
        self.assertTrue(get_response.data)
        [self.assertTrue(data['id']) for data in get_response.data]

    def test_create_contact_without_state(self):

        url = reverse('contacts:contact-create-list')
        data = {
            'first_name': "Rapast",
            'last_name': "Eme",
            # 'mobile': "+17898823654",
            'email': "zombie@zombie.com",
            # 'state': "AZ",
            'city': "jedi",
            'zip_code': "50578-4545",
            'address': "112 Edem Road, Ekwulobia",
        }
        self.client.credentials(**self.auth)
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data)
        self.assertIn('This field is required.', response.data['state'])
        self.assertIn('This field is required.', response.data['mobile'])

    def test_create_contact_invalid_email(self):

        url = reverse('contacts:contact-create-list')
        data = {
            'first_name': "Chinemerem",
            'last_name': "Eme-Okeke",
            'mobile': "+17898823654",
            'email': "zombie@zombie",
            'state': "AZ",
            'city': "jedi",
            'zip_code': "50578-4545",
            'address': "112 Edem Road, Ekwulobia",
        }
        self.client.credentials(**self.auth)
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data)
        self.assertIn('Enter a valid email address.', response.data['email'])


class RetrieveUpdateDeleteContact(TestUserMixin, APITestCase):

        def create_contact(self):
            url = reverse('contacts:contact-create-list')
            data = {
                'first_name': "Gomu Gomu",
                'last_name': "Goku",
                'mobile': "+17898823654",
                'email': "gomu@zombie.com",
                'state': "AZ",
                'city': "jedi",
                'zip_code': "50578-4545",
                'address': "112 Edem Road, Ekwulobia",
            }
            self.client.credentials(**self.auth)
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(response.data)
            self.assertTrue(response.data['owner'])
            return response.data['id']

        def test_get_user(self):
            contact_pk = self.create_contact()
            url = reverse('contacts:single-contact', kwargs={'pk': contact_pk})
            response = self.client.get(url)
            self.assertTrue(response.data)
            # print(response.data)

        def test_patch_user_email(self):
            contact_pk = self.create_contact()
            url = reverse('contacts:single-contact', kwargs={'pk': contact_pk})

            data = {
                'email': "fcuk@zombie.com"
            }
            response = self.client.patch(url, data=data, format='json')
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        # def test_put_user(self):
        #     contact_pk = self.create_contact()
        #     url = reverse('contacts:single-contact', kwargs={'pk': contact_pk})
        #     data = {
        #         'first_name': "Yanki",
        #         'last_name': "Twizzy",
        #         'mobile': "+14898823654",
        #         'email': "zoe@zombie.com",
        #         'state': "AZ",
        #         'city': "jedi",
        #         'zip_code': "50578-4545",
        #         'address': "115 Edem Road, Ekwulobia",
        #     }
        #     response = self.client.put(url, data=data, format='json')
        #     print(response.data)
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        #     self.assertTrue(response.data)




# class RetrieveUpdateDeleteContact(TestContactMixin, APITestCase):
#
#     def test_get_user(self):
#         url = reverse('contacts:single-contact', kwargs={'pk': self.contact_pk})
#         self.client.credentials(**self.auth)
#         response = self.client.get(url)
#         print(response.data)

