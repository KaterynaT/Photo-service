# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20160807_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='whiskers',
        ),
    ]
