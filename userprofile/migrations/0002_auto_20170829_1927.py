# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyprofile',
            name='facultyPostForLeave',
            field=models.CharField(blank=True, choices=[('head', 'head'), ('director', 'director')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='staffPostForLeave',
            field=models.CharField(blank=True, choices=[('registrar', 'registrar'), ('deanacad', 'dean academics'), ('ccc', 'cordinator computer center'), ('hodece', 'hod ECE'), ('hodcse', 'hod CSE'), ('hodme', 'hod ME'), ('dean', 'dean'), ('iw', 'incharge workshop')], max_length=100, null=True),
        ),
    ]