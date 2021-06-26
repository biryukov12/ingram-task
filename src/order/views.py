from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('external_id', 'status')
    ordering_fields = ('id', 'status', 'created_at')

    def update(self, request, *args, **kwargs):
        order_object = self.get_object()
        if order_object.status == 'new':
            data = request.data
            order_object.external_id = data['external_id']
            order_object.save()
            return Response(OrderSerializer(order_object).data)
        else:
            return Response(OrderSerializer(order_object).data)

    def destroy(self, request, *args, **kwargs):
        order_object = self.get_object()
        if order_object.status != 'accepted':
            order_object.delete()
        return Response(OrderSerializer(order_object).data)


    @action(methods=['post'], detail=True)
    def accept(self, request, pk=None):
        order_object = self.get_object()
        order_object.status = 'accepted'
        order_object.save()
        return Response(OrderSerializer(order_object).data)

    @action(methods=['post'], detail=True)
    def fail(self, request, pk=None):
        order_object = self.get_object()
        order_object.status = 'failed'
        order_object.save()
        return Response(OrderSerializer(order_object).data)
