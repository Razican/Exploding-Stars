from django.db import models

# Create your models here.
class Airburst(models.Model):
	total_radiated_energy_j = models.DecimalField(max_digits=15, decimal_places=2)
	calculated_total_impact_energy_kt = models.DecimalField(max_digits=15, decimal_places=2)
	latitude_deg = models.CharField(max_length=200)
	longitude_deg = models.CharField(max_length=200)
	date_time_peak_brightness_ut = models.CharField(max_length=200)
	altitude_km = models.DecimalField(max_digits=15, decimal_places=2)