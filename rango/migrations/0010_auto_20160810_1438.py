# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_document_whiskers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='whiskers',
            field=models.ImageField(default='whiskers_images/beard_PNG6268.png', upload_to=b''),
        ),
    ]
