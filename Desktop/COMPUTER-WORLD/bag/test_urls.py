from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bag.views import view_bag, add_to_bag, adjust_bag, remove_from_bag



class TestbagUrls(SimpleTestCase):
    def test_bag_url_is_resolved(self):
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)

    def test_add_to_bag_url_is_resolved(self):
        url = reverse('add_to_bag', args=['some-slug'])
        self.assertEquals(resolve(url).func, add_to_bag)

    def test_adjust_bag_url_is_resolved(self):
        url = reverse('adjust_bag', args=['some-slug'])
        self.assertEquals(resolve(url).func, adjust_bag)

    def test_remove_from_bag_url_is_resolved(self):
        url = reverse('remove_from_bag', args=['some-slug'])
        self.assertEquals(resolve(url).func, remove_from_bag)