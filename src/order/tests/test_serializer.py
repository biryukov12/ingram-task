from unittest import TestCase


from order.models import Product, Order
from order.serializers import ProductSerializer


class OrderSerializerTestCase(TestCase):
    def test_product(self):
        product = Product.objects.create(name='Same Product')
        serializer_data = ProductSerializer(product).data
        print(serializer_data)
        expected_data = {
            'id': product.id,
            'name': 'Same Product'
        }
        self.assertEqual(serializer_data, expected_data)

    def test_order_without_details(self):
        order = Order.objects.create(external_id='000000')
        serializer_data = ProductSerializer(order).data
        print('S: ', serializer_data)
        expected_data = {
            'id': order.id,
        }
        self.assertEqual(serializer_data, expected_data)
