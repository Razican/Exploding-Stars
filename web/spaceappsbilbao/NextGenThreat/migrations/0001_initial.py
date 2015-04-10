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
                ('total_radiated_energy_j', models.DecimalField(max_digits=5, decimal_places=2)),
                ('calculated_total_impact_energy_kt', models.DecimalField(max_digits=5, decimal_places=2)),
                ('latitude_deg', models.CharField(max_length=200)),
                ('longitude_deg', models.CharField(max_length=200)),
                ('date_time_peak_brightness_ut', models.CharField(max_length=200)),
                ('altitude_km', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]
