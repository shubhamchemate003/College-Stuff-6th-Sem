# Generated by Django 3.2.9 on 2021-12-01 18:56

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=app.models.Item.upload_to, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='item',
            name='original_price',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
    ]