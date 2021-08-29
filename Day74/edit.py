from tempfile import NamedTemporaryFile
import csv
import shutil

def linea(line,index,error,correct):
	if line[index]  == error:
		line[index] = correct
	return line

def modifyFile(type, log, namefile, c1, c2, c3, c4, c5):
	#NEW: type = new || log ||columnas (c*) 0,1,2,3,6
	#columnas edit 1,2,3,4,9
	logError = open(log,'w+')

	name = 'new.csv'
	tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
	with open(namefile, newline='') as csvfile, tempfile:
		content = csv.reader(csvfile, delimiter=";", quotechar="|")
		writeCont = csv.writer(tempfile, delimiter=";", quotechar="|")
		cont = 0
		for line in content:
			if cont:
				linea(line,c5,'Backoffice','Back Office')
				linea(line,c2,'017-405E5','9997')
				linea(line,c2,'C391','12391')
				linea(line,c2,'E535','14535')
				if type == 'edit':
					if line[0] == '':
						logError.write(str(line) + "\n")

				if line[c1] == '' or line[c2] == '' or line[c3] == '' or line[c4] == '':
					logError.write(str(line) + "\n")

				writeCont.writerow(line)
				print(line)
			else:
				writeCont.writerow(line)
				cont += 1

	shutil.move(tempfile.name, name)

modifyFile('new','LogErrorNew.txt', 'NEW_20190424.csv', 0, 1, 2, 3, 6)
# modifyFile('edit','LogErrorEdit.txt', 'EDIT_20201021.csv', 1, 2, 3, 4, 8)