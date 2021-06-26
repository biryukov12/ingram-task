from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from order.models import Order, Product, OrderDetail


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('name',)


class OrderDetailSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderDetail
        fields = (
            'id',
            'product',
            'amount',
            'price'
        )


class OrderSerializer(ModelSerializer):
    details = OrderDetailSerializer(many=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
            'created_at',
            'external_id',
            'details'
        )

    def create(self, *args, **kwargs):
        order = Order.objects.create(external_id=self.context.get('request').data.get('external_id'))
        OrderDetail.objects.bulk_create(
            [OrderDetail(**order_detail, order=order, product=Product.objects.get(**order_detail.pop('product')))
             for order_detail in self.context.get('request').data.get('details')]
        )
        return order
