# Generated by Django 3.2 on 2021-05-30 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mobiles', '0003_auto_20210530_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='model_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='star1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='star2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='star3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='star4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comments',
            name='star5',
            field=models.IntegerField(default=0),
        ),
    ]
