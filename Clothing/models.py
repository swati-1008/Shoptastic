from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clothing(models.Model):
    product_id = models.CharField(max_length=10, unique=True)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()
    product_dimensions = models.CharField(max_length=50)
    launch_date = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    asin = models.CharField(max_length=30)
    origin = models.CharField(max_length=20)
    department = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)
    average_customer_rating = models.FloatField(default=0)
    best_sellers = models.CharField(max_length=200, blank=True)
    model_rating = models.FloatField(default=0)

class Features(models.Model):
    pid = models.ForeignKey(Clothing, on_delete=models.CASCADE, to_field='product_id')
    features = models.CharField(max_length=500)

class Comments(models.Model):
    # pid = models.ForeignKey(Clothing, on_delete=models.CASCADE, to_field='product_id')
    pid = models.CharField(max_length=10)
    # uid = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', related_name='clothing_uid')
    uid = models.CharField(max_length=10)
    rating = models.FloatField(default=0)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField()