# Generated by Django 3.2.9 on 2021-12-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First Name'),
        ),
    ]