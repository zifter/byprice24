# Generated by Django 3.2.9 on 2021-12-03 17:13
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstate',
            name='rating',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]