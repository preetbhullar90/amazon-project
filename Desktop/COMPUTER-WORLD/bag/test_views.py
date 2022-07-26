from django.test import TestCase, Client
from django.urls import reverse


class TestReservationsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.view_bag_url = reverse('view_bag')
        self.add_to_bag_url = reverse('add_to_bag', args=['1'])
        self.adjust_bag_url = reverse('adjust_bag', args=['1'])
        self.remove_from_bag_url = reverse('remove_from_bag', args=['1'])

    def test_view_bag_GET(self):
        response = self.client.get(self.view_bag_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_view_add_to_bag_GET(self):
        response = self.client.get(self.add_to_bag_url)
        self.assertEquals(response.status_code, 404)

    def test_view_adjust_bag_GET(self):
        response = self.client.get(self.adjust_bag_url)
        self.assertEquals(response.status_code, 404)

    def test_view_remove_from_bag_GET(self):
        response = self.client.get(self.remove_from_bag_url)
        self.assertEquals(response.status_code, 500)

        response = self.client.post(self.view_bag_url)
        self.assertEquals(response.status_code, 200)

        response = self.client.post(self.add_to_bag_url)
        self.assertEquals(response.status_code, 404)

        response = self.client.post(self.adjust_bag_url)
        self.assertEquals(response.status_code, 404)

        response = self.client.post(self.remove_from_bag_url)
        self.assertEquals(response.status_code, 500)
