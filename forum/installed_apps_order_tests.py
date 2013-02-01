from django.conf import settings

from django_nose import FastFixtureTestCase as TestCase


class AppOrderTest(TestCase):
    """Ensures the apps are in the order as required by their authors."""

    def setUp(self):
        self.apps = {
            app: order for order, app in enumerate(settings.INSTALLED_APPS)
        }

    def test_forum(self):
        """'forum' goes at the beginning cf.
        https://github.com/ndarville/pony-forum/issues/60.
        """
        if 'forum' in self.apps:
            self.assertEquals(self.apps['forum'], 0)

    def test_django_nose(self):
        """'django_nose' comes after 'South' cf.
        https://github.com/jbalogh/django-nose/blob/master/README.rst#using-with-south.
        """
        if 'django_nose' in self.apps and 'south' in self.apps:
            self.assertTrue(self.apps['django_nose'] > self.apps['south'])

    def test_django_admin_bootstrapped(self):
        """'django_admin_bootstrapped comes before 'django.contrib.admin' cf.
        https://github.com/riccardo-forina/django-admin-bootstrapped/blob/master/README.md.
        """
        if 'django_admin_bootstrapped' and 'django.contrib.admin' in self.apps:
            self.assertTrue(self.apps['django_admin_bootstrapped'] < self.apps['django.contrib.admin'])
