from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Furniture(models.Model):
    product_id = models.CharField(max_length=10, unique=True)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    colour = models.CharField(max_length=20)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()
    product_dimensions = models.CharField(max_length=50)
    assembly_required = models.CharField(max_length=200)
    primary_material = models.CharField(max_length=50)
    finish_type = models.CharField(max_length=50)
    item_shape = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=100)
    origin = models.CharField(max_length=20)
    asin = models.CharField(max_length=30)
    average_customer_rating = models.FloatField(default=0)
    best_sellers = models.CharField(max_length=200, blank=True)
    launch_date = models.CharField(max_length=50)

class Features(models.Model):
    pid = models.ForeignKey(Furniture, on_delete=models.CASCADE, to_field='product_id')
    material = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=70)
    weight = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    assembly_required = models.CharField(max_length=200)

class Comments(models.Model):
    pid = models.ForeignKey(Furniture, on_delete=models.CASCADE, to_field='product_id')
    uid = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', related_name='furniture_uid')
    rating = models.FloatField(default=0)
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField()