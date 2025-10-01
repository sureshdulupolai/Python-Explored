from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product,through='CartItem')

    class Meta:
        db_table="cart"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=0)

    class Meta:
        db_table="cart_item"
