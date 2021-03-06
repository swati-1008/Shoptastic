# Generated by Django 3.2 on 2021-06-01 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=10)),
                ('uid', models.CharField(max_length=10)),
                ('rating', models.FloatField(default=0)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_desc', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('colour', models.CharField(max_length=20)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('image4', models.ImageField(upload_to='')),
                ('image5', models.ImageField(upload_to='')),
                ('os', models.CharField(max_length=10)),
                ('ram', models.CharField(max_length=10)),
                ('product_dimensions', models.CharField(max_length=50)),
                ('batteries', models.CharField(max_length=100)),
                ('item_model_number', models.CharField(max_length=10)),
                ('wireless_features', models.CharField(max_length=1000)),
                ('special_features', models.CharField(max_length=1000)),
                ('display', models.CharField(max_length=1000)),
                ('camera', models.CharField(max_length=200)),
                ('form_factor', models.CharField(max_length=100)),
                ('battery_power', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=20)),
                ('asin', models.CharField(max_length=30)),
                ('average_customer_rating', models.FloatField(default=0)),
                ('best_sellers', models.CharField(max_length=200)),
                ('launch_date', models.CharField(max_length=50)),
                ('manufacture_address', models.CharField(max_length=200)),
                ('generic_name', models.CharField(max_length=20)),
                ('model_rating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.CharField(max_length=500)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mobiles.mobiles', to_field='product_id')),
            ],
        ),
    ]
