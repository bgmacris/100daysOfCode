import csv
from random import randint, choice

def gen_ip():
	type_device = ['pc', 'mobile', 'laptop', 'raspberry']
	parts_ip = []
	for i in range(3):
		part = ''.join([str(randint(1,9)) for i in range(randint(1,3))])
		parts_ip.append(part)
	return ['.'.join(parts_ip), choice(type_device)]

with open('IP.csv', 'w', newline='') as file:
	ipwriter = csv.writer(file, delimiter=',', quotechar='|')
	for i in range(500):
		device = gen_ip()
		ipwriter.writerow(device)
