from django.test import TestCase
from aboutus.models import NewsletterUsers


class TestNewslettersModels(TestCase):

    def setUp(self):
        self.newsletterUsers = NewsletterUsers(
            email='test123@gmail.com', date_added='july 8,2022, 6:26 p.m',)

    def test_create_newsletterUsers(self):
        self.assertEquals(self.newsletterUsers.email, 'test123@gmail.com')
        self.assertEquals(self.newsletterUsers.date_added,
                          'july 8,2022, 6:26 p.m')

    def test_newsletterUsers_works(self):
        newsletterUsers = len(NewsletterUsers.objects.all())
        self.assertEquals(newsletterUsers, 0)
