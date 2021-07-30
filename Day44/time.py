"""

API FROM https://www.tomorrow.io/weather-api/

"""


import requests


#URL = 'https://api.tomorrow.io/v4/locations'
URL = 'https://api.tomorrow.io/v4/timelines'
header = {
	'content-type': 'application/json',
	'apikey': ''
}
params = {
	'location': '61043f435313400008dcc515',
	'fields': [
		'temperature', 'temperatureApparent',
		'cloudCover', 'windSpeed',
		'precipitationIntensity',
	],
	'units': 'metric',
	'timesteps': '1d'
}


with requests.get(URL, headers=header, params=params) as REQUEST:
	print(REQUEST.text)
	print(REQUEST.status_code)
	if REQUEST.status_code == 200:
		data = REQUEST.json()
		print(data)
		location_name = 'La Senia'

		values_info = data['data']['timelines'][0]['intervals'][0]['values']
		temp = values_info['temperature']
		sens_temp = values_info['temperatureApparent']
		wind = values_info['windSpeed']
		cloud = values_info['cloudCover']
		precipitation = values_info['precipitationIntensity']

print(f"TEMPERATURA: {temp}\n\
SENSACION TERMINCA: {sens_temp}\n\
VEL. VIENTO: {wind}\n\
NUBLADO: {cloud}\n\
PRECIPITACION: {precipitation}")

