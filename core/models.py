from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    quantity = models.IntegerField('Inventory quantity')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    email = models.CharField('email', max_length=100)

    def __str__(self):
        return self.name




