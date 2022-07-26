from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import all_products, product_detail 



class TestProductUrls(SimpleTestCase):
    def test_all_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_products)

    def test_product_detail_url_is_resolved(self):
        url = reverse('product_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, product_detail)

    

   
