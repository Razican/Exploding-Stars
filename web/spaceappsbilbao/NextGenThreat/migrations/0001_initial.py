# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airburst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radiated_energy', models.BigIntegerField()),
                ('impact_energy', models.DecimalField(max_digits=10, decimal_places=3)),
                ('latitude', models.DecimalField(max_digits=8, decimal_places=5)),
                ('longitude', models.DecimalField(max_digits=8, decimal_places=5)),
                ('date', models.DateTimeField()),
                ('altitude', models.DecimalField(null=True, max_digits=5, decimal_places=2)),
            ],
        ),
    ]
