from itertools import product
from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products.models import Product



class TestNewslettersModels(TestCase):

    def setUp(self):
        self.order = Order(
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
       

        self.product = Product(
            sku='45353er',
            name='preet',
            description='this is description',
            has_sizes=True,
            price=34.5,
            rating=34.5,
            weight=34.5,
            dimension='34',
        )
        
        self.orderlineitem = OrderLineItem(
            order=self.order,
            product=self.product,
            product_size='24,26,29',
            quantity=234,
            lineitem_total=23.5,
        )

    def test_create_order(self):
        self.assertEquals(self.order.order_number, '45353er')
        self.assertEquals(self.order.full_name, 'preet')
        self.assertEquals(self.order.email, 'test123@gmail.com')
        self.assertEquals(self.order.phone_number, 64647547677)
        self.assertEquals(self.order.country, 'england')
        self.assertEquals(self.order.postcode, '45646')
        self.assertEquals(self.order.town_or_city, 'hayes')
        self.assertEquals(self.order.street_address1, '123 hayes')
        self.assertEquals(self.order.street_address2, '123 hayes')
        self.assertEquals(self.order.county, 'london')
        self.assertEquals(self.order.date, 'july 8,2022, 6:26 p.m')
        self.assertEquals(self.order.delivery_cost, 5.43)
        self.assertEquals(self.order.order_total, 5.43)
        self.assertEquals(self.order.grand_total, 5.43)

    def test_create_orderlineitem(self):
        self.assertEquals(self.orderlineitem.order, self.order)
        self.assertEquals(self.orderlineitem.product, self.product)
        self.assertEquals(self.orderlineitem.product_size, '24,26,29')
        self.assertEquals(self.orderlineitem.quantity, 234)
        self.assertEquals(self.orderlineitem.lineitem_total, 23.5)

    def test_create_product(self):
        self.assertEquals(self.product.sku, '45353er')
        self.assertEquals(self.product.name, 'preet')
        self.assertEquals(self.product.description, 'this is description')
        self.assertEquals(self.product.has_sizes, True)
        self.assertEquals(self.product.price, 34.5)
        self.assertEquals(self.product.rating, 34.5)
        self.assertEquals(self.product.weight, 34.5)
        self.assertEquals(self.product.dimension, '34')

    def test_order_works(self):
        order = len(Order.objects.all())
        self.assertEquals(order, 0)
        
        
    def test_orderlineitem_works(self):
        orderlineitem = len(OrderLineItem.objects.all())
        self.assertEquals(orderlineitem, 0)
        

    def test_product_works(self):
        product = len(Product.objects.all())
        self.assertEquals(product, 0)
