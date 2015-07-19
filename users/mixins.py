__author__ = 'adede08'
from users.models import ContactOwner


class LoginUserMixin(object):
    """ This class set's up a TEST user. """

    EMAIL = 'ovute.ugwoke@foo.com'
    PASSWORD = 'aVadacadavRa02'
    user = None
    auth = None

    def setUp(self):
        user = ContactOwner.objects.create_user(
            email=self.EMAIL,
            password=self.PASSWORD,
        )
        assert user
        self.user = user
        if user.token:
            self.auth = {'HTTP_AUTHORIZATION': 'Token: {0}'.format(user.token)}
