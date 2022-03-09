# Generated by Django 3.2.8 on 2022-03-08 15:35
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0018_alter_productpage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.category'),
        ),
        migrations.AddField(
            model_name='productpage',
            name='preview_url',
            field=models.CharField(max_length=256, null=True),
        ),
    ]