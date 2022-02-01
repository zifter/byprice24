# Generated by Django 3.2.9 on 2021-12-13 21:20
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_alter_productstate_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='description',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MOBILE', 'Mobile'), ('NOTEBOOK', 'Notebook'), ('DISPLAY', 'Monitor'), ('DESKTOP', 'Desktop'), ('TV', 'TV'), ('TABLET', 'Tablet'), (
                'HEADPHONE', 'Headphones'), ('LEGO', 'ConstructionSet'), ('COSMETIC', 'Cosmetic'), ('BOOK', 'Book'), ('SMART_GADGET', 'SmartGadget')], max_length=62),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=512),
        ),
    ]
