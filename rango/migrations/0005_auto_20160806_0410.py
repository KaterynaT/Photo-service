# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_whiskers_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whiskers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='whiskers',
            name='scale_x',
        ),
        migrations.RemoveField(
            model_name='whiskers',
            name='scale_y',
        ),
        migrations.RemoveField(
            model_name='whiskers',
            name='whiskers',
        ),
        migrations.RemoveField(
            model_name='whiskers',
            name='x',
        ),
        migrations.RemoveField(
            model_name='whiskers',
            name='y',
        ),
        migrations.AddField(
            model_name='whiskers',
            name='image',
            field=models.ImageField(upload_to='media/whiskers_images', blank=True),
        ),
        migrations.AddField(
            model_name='whiskers',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
