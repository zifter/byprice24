# Generated by Django 3.2.12 on 2022-04-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0020_alter_productpage_category_preview_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplace',
            name='delivery',
            field=models.BooleanField(default=False),
        ),
    ]