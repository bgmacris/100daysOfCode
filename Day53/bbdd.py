import csv
import os

class DataBase:
	def __init__(self, bbdd, data=None):
		self.bbdd = f'databases/{str(bbdd)}.csv'

	def create_bbdd(self, data):
		with open(self.bbdd, 'w', newline='') as file:
			datawrite = csv.writer(file, delimiter=',', quotechar='|')
			datawrite.writerow(data['columns'])

	def put_data(self, data):
		data = data.replace(' ', '')
		try:
			data = [i.split(',') for i in data.split(';')]
		except Exception as e:
			return e
		with open(self.bbdd, 'a', newline='') as file:
			read_columns = csv.reader(file, delimiter=',', quotechar='|')
			datawrite = csv.writer(file, delimiter=',', quotechar='|')

	def get_columns(self):
		with open(self.bbdd, 'r') as file:
			line = file.readline().replace('\n', '')
			return line.split(',')


	def get_data(self, bbdd):
		with open(self.bbdd, 'r') as file:
			lines = file.readlines()
			print(lines)


	def get_all_bbdd(self):
		databases = [f.name.replace('.csv', '') for f in os.scandir('databases') if not(f.is_dir())]
		return databases
