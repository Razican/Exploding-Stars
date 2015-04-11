from django.core.management.base import BaseCommand, CommandError
from NextGenThreat.models import Airburst
from datetime import datetime
from dateutil import parser
import requests

class Command(BaseCommand):
	help = 'Updates project\'s database from NASA sources'
	url = 'https://data.nasa.gov/resource/mc52-syum.json'

	def handle(self, *args, **options):
		count = Airburst.objects.count()
		if count > 0:
			date_where = '?$where=date_time_peak_brightness_ut>\''+ Airburst.objects.all().latest('date').date.strftime('%Y-%m-%dT%H:%M:%S')+'\''
		else:
			date_where = ''

		request = requests.get(self.url + date_where)

		if (request.status_code == 200):
			data = request.json()

			if len(data) > 0:
				for bolide in data:
					burst = Airburst()
					burst.radiated_energy = int(bolide['total_radiated_energy_j'])
					burst.impact_energy = float(bolide['calculated_total_impact_energy_kt'])
					burst.date = parser.parse(bolide['date_time_peak_brightness_ut']+' UTC')
					burst.altitude = bolide.get('altitude_km', None)
					if burst.altitude != None:
						burst.altitude = float(burst.altitude)

					burst.latitude = float(bolide['latitude_deg'][:-1])
					if bolide['latitude_deg'][-1:] == 'S':
						burst.latitude *= -1
					burst.longitude = float(bolide['longitude_deg'][:-1])
					if bolide['longitude_deg'][-1:] == 'W':
						burst.longitude *= -1

					burst.save()
				#TODO: send push notification
