# Generated by Django 2.2.9 on 2021-05-13 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobiles_uid', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
