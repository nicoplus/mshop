# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 07:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20170719_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pollitem',
            name='poll',
        ),
        migrations.DeleteModel(
            name='VoteCheck',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='PollItem',
        ),
    ]
