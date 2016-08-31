# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whiskers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('whiskers', models.ImageField(upload_to='whiskers_images')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('scale_x', models.IntegerField()),
                ('scale_y', models.IntegerField()),
            ],
        ),
    ]
