from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return u'{} ({} PLN)'.format(self.name, self.price)


class Order(models.Model):
    user = models.ForeignKey(User)
    address = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'{}/{}'.format(self.user.username, self.address)


class OrderPosition(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order)

    def __unicode__(self):
        return u'{} ({} szt.)'.format(self.product.name, self.quantity)

    @property
    def total_price(self):
        return self.product.price * self.quantity
