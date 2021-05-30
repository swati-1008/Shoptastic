from django.db import models
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.

class Mobiles(models.Model):
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
    os = models.CharField(max_length=10)
    ram = models.CharField(max_length=10)
    product_dimensions = models.CharField(max_length=50)
    batteries = models.CharField(max_length=100)
    item_model_number = models.CharField(max_length=10)
    wireless = models.CharField(max_length=1000)
    special = models.CharField(max_length=1000)
    display = models.CharField(max_length=1000)
    camera = models.CharField(max_length = 200)
    form_factor = models.CharField(max_length=100)
    battery_power = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    origin = models.CharField(max_length=20)
    asin = models.CharField(max_length=30)
    average_customer_rating = models.FloatField(default=0)
    best_sellers = models.CharField(max_length=200)
    launch_date = models.CharField(max_length=50)
    manufacture_address = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=20)

class Features(models.Model):
    pid = models.ForeignKey(Mobiles, on_delete=models.CASCADE, to_field='product_id')
    features = models.CharField(max_length=500)

class Comments(models.Model):
    # pid = models.ForeignKey(Mobiles, on_delete=models.CASCADE, to_field='product_id')
    pid = models.CharField(max_length=10)
    # uid = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', related_name='mobiles_uid')
    uid = models.CharField(max_length=10)
    rating = models.FloatField(default=0)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField()