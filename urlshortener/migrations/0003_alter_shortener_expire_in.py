# Generated by Django 4.0.2 on 2022-02-21 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_alter_shortener_expire_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='expire_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 10, 15, 35, 270426)),
        ),
    ]
