__author__ = 'Ikechukwu'
from users.models import ContactOwner


class TestUserMixin(object):
    """ This class set's up a TEST user. """

    EMAIL = 'ikdme@yahoo.com'
    PASSWORD = 'aVadacadavRa02',

    def setUp(self):
        user = ContactOwner.objects.create_user(
            email = self.EMAIL,
            password = self.PASSWORD
        )
        assert(user)
        assert(user.token)
        self.user = user
        self.auth = {'HTTP_AUTHORIZATION': 'Token: {0}'.format(user.token)}