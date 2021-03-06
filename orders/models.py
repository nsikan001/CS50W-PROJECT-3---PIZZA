from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return f"{self.name} - {self.image_url}"


class Regular_pizza(models.Model):
    name = models.CharField(max_length=65)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"


class Sicilian_pizza(models.Model):
    name = models.CharField(max_length=65)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"


class Topping(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    name = models.CharField(max_length=65)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"


class Pasta(models.Model):
    name = models.CharField(max_length=65)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Salad(models.Model):
    name = models.CharField(max_length=65)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Dinner_platter(models.Model):
    name = models.CharField(max_length=65)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} - {self.large}"

class User_order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    topping_allowance = models.IntegerField(default=0)
    status = models.CharField(max_length=64, default='initiated')

    def __str__(self):
        return f"{self.user} - {self.order_number} - {self.status} Topping_allowance: {self.topping_allowance}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.name} - ${self.price} - {self.quantity}"


class Order_count(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return f"Order no: {self.count}  "


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prod_name = models.CharField(max_length=65)
    prod_price = models.FloatField()
    prod_qty = models.IntegerField()
    is_ordered = models.CharField(max_length=20)
    admin_comment = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.user} - {self.prod_name} - ${self.prod_price} - {self.prod_qty} - {self.is_ordered} - {self.admin_comment}"

    def price(self):
        return (self.prod_price)

    def amount(self):
        return (self.prod_qty * self.prod_price)

