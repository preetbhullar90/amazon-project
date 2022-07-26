from django.test import TestCase, Client
from django.urls import reverse
from products.models import Category, Product
import tempfile



class TestProductsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.category_url = reverse('product_detail', args=['1'])
        self.product_url = reverse('products')
       

        self.category = Category.objects.create(
            name = 'preet',
            friendly_name = 'monitor'
        )

        self.product = Product.objects.create(
            category = self.category,
            sku='45353er',
            name='preet',
            description='this is description',
            has_sizes=True,
            price=34.5,
            rating=34.5,
            image_url = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image1 = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            image2 = tempfile.NamedTemporaryFile(suffix=".jpg").name,
            weight=34.5,
            dimension='34',
        )

        
        

    def test_category_GET(self):
        response = self.client.get(self.category_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_GET(self):
        response = self.client.get(self.product_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        
        
        response = self.client.post(self.category_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Category.objects.all()), 1)
        
        response = self.client.post(self.product_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Product.objects.all()), 1)
        

   