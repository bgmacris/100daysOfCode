from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from bs4 import BeautifulSoup
import requests
import os
import img2pdf
import threading
import time


# Create your views here.
def index(request):
    if request.method == "POST":
        capitulo = request.POST
        print(capitulo['capitulo'])
        api_manga(request, capitulo['capitulo'])
        return FileResponse(open(f"C:\\Users\\Bogdan\\Desktop\\pyapps\\framework\\la_cueva\\apps\\reed_manga\\manga\\manga_capitulo{capitulo['capitulo']}.pdf", "rb"), content_type="aplication/pdf")

    return render(request, 'reed_manga/index.html')


def delete_png():
    dir = 'C:\\Users\\Bogdan\\Desktop\\pyapps\\framework\\la_cueva\\apps\\reed_manga\\manga'
    for file in os.listdir(dir):
        os.remove(os.path.join(dir, file))


def create_pdf(name):
    dir = 'C:\\Users\\Bogdan\\Desktop\\pyapps\\framework\\la_cueva\\apps\\reed_manga\\manga\\'
    imagenes = [dir + archivos for archivos in os.listdir(dir)]
    print(imagenes)
    
    with open(f"C:\\Users\\Bogdan\\Desktop\\pyapps\\framework\\la_cueva\\apps\\reed_manga\\manga\\manga_capitulo{name}.pdf", "wb") as pdf:
        pdf.write(img2pdf.convert(imagenes))


def download_img(name):
    os.system(name)

def api_manga(request, capitulo):
    delete_png()

    url = f"https://submanga.io/manga/one-piece-online/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page = 1
    for a in soup.find_all('a', href=True):
        if a.text != None:
            if len(a.text.split()) >= 3:
                if capitulo == a.text.split()[2]:
                    for i in range(27):
                        url_capitulo = a['href'] + f'/{page}'
                        response_capitulo = requests.get(url_capitulo)
                        soup_capitulo = BeautifulSoup(
                            response_capitulo.content, 'html.parser')
                        for img in soup_capitulo.find_all('img', class_='img-responsive scan-page', src=True):
                            url = img['src']
                            nombre_img = f'C:\\Users\\Bogdan\\Desktop\\pyapps\\api\\test.py {url[1:]} {url[-7:-5]}'
                            threading.Thread(target=download_img, args=(nombre_img,)).start()
                        page += 1

    create_pdf(capitulo)
