# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0023_remove_subject_practice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['name']},
        ),
    ]
