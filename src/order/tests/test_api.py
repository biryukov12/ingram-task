from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class OrdersApiTestCase(APITestCase):
    def test_response_status(self):
        response = self.client.get(reverse('order-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
