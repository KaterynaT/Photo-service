# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_watermark'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watermark',
        ),
    ]
