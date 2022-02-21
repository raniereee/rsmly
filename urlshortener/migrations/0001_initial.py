# Generated by Django 4.0.2 on 2022-02-21 12:38

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expire_in', models.DateTimeField(default=datetime.datetime(2022, 3, 23, 9, 38, 2, 97838))),
                ('times_followed', models.PositiveIntegerField(default=0)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=15, unique=True)),
                ('name_short_url', models.CharField(default=uuid.uuid1, max_length=15, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]