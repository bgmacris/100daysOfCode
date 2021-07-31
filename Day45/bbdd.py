import csv

class DataBase:
	def __init__(self, bbdd, data=None):
		self.data = str(bbdd) + '.csv'

	def create_bbdd(self, bbdd, data):
		bbdd = f'databases/bbdd.csv'
		with open(bbdd, 'w', newline='') as file:
			datawrite = csv.writer(file, delimiter=',', quotechar='|')
			datawrite.writerow(data['columns'])



	def get_data(self, bbdd):
		with open(self.bbdd, 'r') as file:
			lines = file.readlines()
			print(lines)

