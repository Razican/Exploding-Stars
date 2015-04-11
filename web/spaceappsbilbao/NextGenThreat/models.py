from django.db import models

class Airburst(models.Model):
	radiated_energy = models.BigIntegerField()
	impact_energy = models.DecimalField(max_digits=10, decimal_places=3)
	latitude = models.DecimalField(max_digits=8, decimal_places=5)
	longitude = models.DecimalField(max_digits=8, decimal_places=5)
	date = models.DateTimeField()
	altitude = models.DecimalField(max_digits=5, decimal_places=2, null=True)

	def __str__(self):
		return "Total radiated energy " + str(self.radiated_energy)
