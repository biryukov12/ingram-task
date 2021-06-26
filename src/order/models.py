from django.db import models


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'new'),
        ('accepted', 'accepted'),
        ('failed', 'failed')
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    external_id = models.CharField(max_length=128, unique=True)
    products = models.ManyToManyField(to='Product', through='OrderDetail')

    def __str__(self):
        return f'{self.external_id}'


class Product(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.order} :: {self.product} :: {self.amount} :: {self.price}'
