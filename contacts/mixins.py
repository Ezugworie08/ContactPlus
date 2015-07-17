__author__ = 'Ikechukwu'
from users.models import ContactOwner
from contacts.models import Contact


class TestUserMixin(object):
    """ This class set's up a TEST user. """

    EMAIL = 'rapast@yahoo.com'
    PASSWORD = 'aVadacadavRa02'
    user = None
    auth = None

    def setUp(self):
        user = ContactOwner.objects.create_user(
            email=self.EMAIL,
            password=self.PASSWORD,
        )
        assert user
        user.login()
        assert user.token

        self.user = user
        self.auth = {'HTTP_AUTHORIZATION': 'Token: {0}'.format(user.token)}


class TestContactMixin(object):
    """
    This class creates a TEST contact and also, a test user
    """

    EMAIL = 'rapast@yahoo.com'
    PASSWORD = 'aVadacadavRa02'
    user = None
    auth = None
    contact = None
    contact_pk = None
    model = Contact

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

    def setUp(self):
        user = ContactOwner.objects.create_user(
            email=self.EMAIL,
            password=self.PASSWORD,
        )
        assert user
        user.login()
        assert user.token

        self.user = user
        self.auth = {'HTTP_AUTHORIZATION': 'Token: {0}'.format(user.token)}

        self.data['owner'] = user
        new_contact = self.model.objects.create(**self.data)
        print(new_contact)
        assert new_contact
        assert new_contact.id
        self.contact = new_contact
        self.contact_pk = new_contact.id
