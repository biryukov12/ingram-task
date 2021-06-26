from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet

router = DefaultRouter()

router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path(r'api/v1/', include(router.urls)),
]
