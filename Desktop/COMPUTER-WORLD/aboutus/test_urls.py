from django.test import SimpleTestCase
from django.urls import reverse, resolve
from aboutus.views import aboutus,newsletter_signup,newsletter_unsubscribe


class TestAboutusUrls(SimpleTestCase):
    def test_aboutus_url_is_resolved(self):
        url = reverse('aboutus')
        self.assertEquals(resolve(url).func, aboutus)
        
        
        
    def test_newsletter_signup_url_is_resolved(self):
        url = reverse('newsletter_signup')
        self.assertEquals(resolve(url).func, newsletter_signup)
        
        
    def test_newsletter_unsubscribe_url_is_resolved(self):
        url = reverse('newsletter_unsubscribe')
        self.assertEquals(resolve(url).func, newsletter_unsubscribe)