from fpdf import FPDF
import os

PATH = os.path.join(os.getcwd(), 'images/')
# orientation='L'
pdf = FPDF(unit = 'cm', format='A3')

#images = [f"{PATH}{i}" for i in os.listdir(PATH)]
images = sorted([f'{PATH}{i}' for i in os.listdir(PATH)])
pdf.add_page()
for img in images:
	pdf.image(img)
pdf.output('file.pdf', 'F')
