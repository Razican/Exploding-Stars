# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NextGenThreat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airburst',
            name='altitude_km',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='airburst',
            name='calculated_total_impact_energy_kt',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='airburst',
            name='total_radiated_energy_j',
            field=models.DecimalField(max_digits=15, decimal_places=2),
        ),
    ]
