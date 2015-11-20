from django.db import models

class User(models.Model):
    address = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    id = models.IntegerField(primary_key=True)
    is_staff = models.BooleanField(default=False)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    paid = models.BooleanField(default=False)

class Orders(models.Model):
    user_id = models.ForeignKey(User)
    order_id = models.ForeignKey(Order)

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    active = models.BooleanField(default=False)
    description = models.TextField()
    stockQuantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Contains(models.Model):
    quantity = models.IntegerField(default=0)
    order_id = models.ForeignKey(Orders)
    product_id = models.ForeignKey(Product)

class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Supplys(models.Model):
    product_id = models.ForeignKey(Product)
    supplier_id = models.ForeignKey(Supplier)



# Create your models here.
