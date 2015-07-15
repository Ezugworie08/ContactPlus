__author__ = 'Ikechukwu'
from users.models import ContactOwner


class TestUserMixin(object):
    """ This class set's up a TEST user. """

    EMAIL = 'ovute.ugwoke@yahoo.com'
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
