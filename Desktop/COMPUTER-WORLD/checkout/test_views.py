from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import Order, OrderLineItem
from products.models import Product
import tempfile


class TestCheckoutViews(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.order_url = reverse('checkout')
        self.orderlineitem_url = reverse('checkout')
        self.product_url = reverse('products')
        
        
        
        
        
        
        self.order = Order.objects.create(
            order_number='45353er',
            full_name='preet',
            email='test123@gmail.com',
            phone_number=64647547677,
            country='england',
            postcode='45646',
            town_or_city='hayes',
            street_address1='123 hayes',
            street_address2='123 hayes',
            county='london',
            date='july 8,2022, 6:26 p.m',
            delivery_cost=5.43,
            order_total=5.43,
            grand_total=5.43,
            )
        
        self.product = Product.objects.create(
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
        
        
        self.orderlineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            product_size='24,26,29',
            quantity=234,
            lineitem_total=23.5,
            )


    def test_order_GET(self):
        response = self.client.get(self.order_url)
        self.assertEquals(response.status_code, 302)
     
        
        
    def test_product_GET(self):
        response = self.client.get(self.order_url)
        self.assertEquals(response.status_code, 302)
        

    def test_orderlineitem_url_GET(self):
        response = self.client.get(self.orderlineitem_url)
        self.assertEquals(response.status_code, 302)
        

    
        order1 = Order.objects.create(
            order_number='45353er',
            full_name='preet',
            email='test123@gmail.com',
            phone_number=64647547677,
            country='england',
            postcode='45646',
            town_or_city='hayes',
            street_address1='123 hayes',
            street_address2='123 hayes',
            county='london',
            date='july 8,2022, 6:26 p.m',
            delivery_cost=5.43,
            order_total=5.43,
            grand_total=5.43,
        )

        response = self.client.post(self.order_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(Order.objects.all()), 2)
        self.assertEquals(len(Product.objects.all()), 1)
        self.assertEquals(len(OrderLineItem.objects.all()), 1)

   

    