from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class Category(models.Model):
   name=models.CharField(max_length=50,null=False,default="")
   slug=AutoSlugField(populate_from='name',unique=True)

   def __str__(self):
      return self.name


class Product(models.Model):
   name=models.CharField(max_length=50,null=False,default='product-name')
   description=models.TextField(null=False)
   price=models.DecimalField(null=False,decimal_places=2,max_digits=8)
   image=models.ImageField(upload_to='products/',default="",null=False)
   category=models.ForeignKey(Category,on_delete=models.PROTECT,default=None,null=True)


   def __str__(self):
      return f'Name : {self.name} |  Price: {self.price}'
