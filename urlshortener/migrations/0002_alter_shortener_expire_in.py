# Generated by Django 4.0.2 on 2022-02-21 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='expire_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 9, 50, 7, 826720)),
        ),
    ]
