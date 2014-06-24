import os
from django.conf import settings
from django.test import TestCase
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()


class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        settings.TEMPLATE_DIRS = (
            os.path.join(os.path.dirname(__file__), 'templates'),
        )
        User.objects.create_user('testuser',
                                 'testuser@example.com',
                                 'testuser')

    def user(self):
        return User.objects.get(username='testuser')
