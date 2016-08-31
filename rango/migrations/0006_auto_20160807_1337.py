# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20160806_0410'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Whiskers',
        ),
        migrations.AddField(
            model_name='document',
            name='whiskers',
            field=models.ImageField(default=1, upload_to='whiskers_images'),
            preserve_default=False,
        ),
    ]
