__author__ = 'Ikechukwu'
from users.models import ContactOwner


class TestUserMixin(object):
    """ This class set's up a TEST user. """

    FIRST_NAME = 'Ikechukwu'
    LAST_NAME = 'Ezugworie'
    EMAIL = 'ikdme@yahoo.com'
    PASSWORD = 'aVadacadavRa02',

    # Lifted directly from the docs.
    # client = APIClient()
    # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    def setUp(self):
        user = ContactOwner.objects.create_user(
            email = self.EMAIL,
            password = self.PASSWORD
        )
        assert(user)
        self.user = user
        self.auth = {'HTTP_AUTHORIZATION': 'Token: {0}'.format(user.token)}