# Generated by Django 3.2.8 on 2021-12-16 15:44
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_auto_20211213_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketplace',
            name='image_logo_url',
        ),
        migrations.RemoveField(
            model_name='marketplace',
            name='rating',
        ),
        migrations.AddField(
            model_name='marketplace',
            name='logo_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productpage',
            name='name',
            field=models.CharField(default='', max_length=62),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='preview_url',
            field=models.URLField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='productpage',
            name='url',
            field=models.URLField(),
        ),
    ]