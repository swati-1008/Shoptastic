# Generated by Django 2.2.9 on 2021-05-13 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('product_dimensions', models.CharField(max_length=50)),
                ('assembly_required', models.CharField(max_length=200)),
                ('primary_material', models.CharField(max_length=50)),
                ('finish_type', models.CharField(max_length=50)),
                ('item_shape', models.CharField(max_length=20)),
                ('manufacturer', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=20)),
                ('asin', models.CharField(max_length=30)),
                ('average_customer_rating', models.FloatField(default=0)),
                ('best_sellers', models.CharField(blank=True, max_length=200)),
                ('launch_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=50)),
                ('dimensions', models.CharField(max_length=70)),
                ('weight', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('assembly_required', models.CharField(max_length=200)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Furniture.Furniture', to_field='product_id')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Furniture.Furniture', to_field='product_id')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='furniture_uid', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
