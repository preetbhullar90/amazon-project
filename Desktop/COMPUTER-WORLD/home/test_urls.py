from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index


class TestHomeUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)
