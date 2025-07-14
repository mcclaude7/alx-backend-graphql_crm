# from django.db import models

# # Create your models here.vkv
# class Customer(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     last_order_date = models.DateTimeField(null=True, blank=True)

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
