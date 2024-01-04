from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    mobile = models.CharField(max_length=20, null=False)



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey('Category',  on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    product_image1 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    product_image4 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date = models.DateField(auto_now_add=True, null=True)





class Feedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
