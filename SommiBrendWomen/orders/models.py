from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    status = models.BooleanField(default=True)
    comments = models.TextField(blank=True, null=None, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=None, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=None, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=None, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар %s" % self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



