# Generated by Django 3.2.9 on 2021-12-12 20:35
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_productstate_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstate',
            name='availability',
            field=models.CharField(choices=[('BackOrder', 'BackOrder'), ('Discontinued', 'Discontinued'), ('InStock', 'InStock'), ('InStoreOnly', 'InStoreOnly'), ('LimitedAvailability', 'LimitedAvailability'), (
                'OnlineOnly', 'OnlineOnly'), ('OutOfStock', 'OutOfStock'), ('PreOrder', 'PreOrder'), ('PreSale', 'PreSale'), ('SoldOut', 'SoldOut')], default='', max_length=24),
        ),
    ]