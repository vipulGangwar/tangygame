# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20161216_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('discription', models.CharField(max_length=1000)),
            ],
        ),
    ]