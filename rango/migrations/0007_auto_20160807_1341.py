# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20160807_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='whiskers',
            field=models.ImageField(null=True, upload_to='whiskers_images', blank=True),
        ),
    ]
