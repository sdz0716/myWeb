# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 11:09
from __future__ import unicode_literals

import UnixTimestampField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serverinfo', '0009_auto_20170612_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlist',
            name='alter_time',
            field=UnixTimestampField.UnixTimestampField(null=True),
        ),
    ]
