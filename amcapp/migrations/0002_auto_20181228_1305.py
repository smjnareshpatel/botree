# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-12-28 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amcapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=800)),
                ('last_name', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
