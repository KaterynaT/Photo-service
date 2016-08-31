# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0012_delete_watermark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watermark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opacity', models.FloatField(default=100)),
                ('x', models.IntegerField(default=0, null=True, blank=True)),
                ('y', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
    ]
