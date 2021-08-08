import sys
import re, requests, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from apiclient.discovery import build
from apiclient.errors import HttpError
import pytube
import pafy
import vlc
import os
import csv
import threading
import time

API_KEY = 'KEY'
SERVICE_NAME = 'youtube'
SERVICE_VERSION = 'v3'

use_api = False
if len(sys.argv) > 1:
	if str(sys.argv[1]) == 'api':
		print("Use Api")
		youtube = build(SERVICE_NAME, SERVICE_VERSION, developerKey=API_KEY)
		use_api = True

def pafy_video(video_id):
	vid = pafy.new(video_id)
	return vid

def youtube_search(options):
	search_response = youtube.search().list(
		q=options,
		part='id,snippet',
	).execute()

	videos = []
	for search_result in search_response.get('items', []):
		if search_result['id']['kind'] == 'youtube#video':
			videos.append(
				(
					f"https://www.youtube.com/watch?v={search_result['id']['videoId']}",
					search_result['snippet']['title'])
			)
	return videos


def scraping_search(cancion):
	query_string = urllib.parse.urlencode({"search_query": cancion})
	formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
	search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
	urls_songs = [f"https://www.youtube.com/watch?v={id}" for id in search_results]
	return urls_songs

def transform_list_to_dict(lista):
	urls = []
	for url in lista[:5]:
		response = requests.get(url, cookies={'CONSENT': 'YES+1'})
		vid = pafy.new(url)
		title = vid.title
		urls.append((url, title))
	videos = {urls.index(i) + 1: i for i in urls}
	return videos


def get_listas():
	try:
		return [f.name.replace('.csv', '') for f in os.scandir('listas/') if not(f.is_dir())]
	except:
		return {'Error': "Extensions File Error"}


def add_to_list(lista, METHOD='GET', data=None):
	iter_lists = get_listas()
	if data != None:
		if not 'title' in data[0] or not 'url' in data[0] or not 'opt' in data[0]:
			return {'Error': "Format list, dict {'opt' and 'title' and 'url'} song"}
	if METHOD == 'GET':
		if lista in iter_lists:
			canciones = []
			with open(f'listas/{lista}.csv', 'r', newline='') as file:
				spamreader = csv.reader(file, delimiter=',', quotechar='|')
				for row in spamreader:
					canciones.append(row)
			return canciones
		else:
			return {'Error': 'Create list'}
	if METHOD == 'PUT':
		try:
			with open(f'listas/{lista}.csv', 'w', newline='') as file:
				spamwriter = csv.writer(file, delimiter=',', quotechar='|')
				spamwriter.writerow(['option', 'title', 'url'])
				for d in data:
					spamwriter.writerow([d['opt'], d['title'], d['url']])
			return True
		except Exception as e:
			print(e)
			return False
	if METHOD == 'ADD':
		try:
			with open(f'listas/{lista}.csv', 'a', newline='') as file:
				spamwriter = csv.writer(file, delimiter=',', quotechar='|')
				for d in data:
					spamwriter.writerow([d['title'], d['url']])
			return True
		except:
			return False
	if METHOD == 'DELETE':
		try:
			os.remove(f'listas/{lista}.csv')
		except Exception as e:
			return e


def play_music(url):
	Instance = vlc.Instance('-I dummy --no-video')
	#Instance = vlc.Instance()
	player = Instance.media_player_new()
	Media = Instance.media_new(str(url))
	Media.get_mrl()
	player.set_media(Media)
	player.play()
	#threading.Thread(target=is_playing_song, args=(player,)).start()
	print("La musica esta sonando. . .")
	while True:
		option = input("Stop -> (S), Pause -> (P), Play -> (R): ")
		if option.upper() == 'S':
			print("Se ha parado la musica")
			player.stop()
			return 'STOP'
		elif option.upper() == 'P':
			print("Se ha pausado la musica")
			player.pause()
		elif option.upper() == 'R':
			print("Se reproduce la musica")
			player.play()
	player.stop()


def search_song_for_list():
	canciones = []
	print("Busca las canciones que quieres añadir en la lista, cuando acabes escribe '-READY'")
	numeracion = 1
	while True:
		cancion = input("Buscar cancion: ")
		if cancion.upper() == '-READY':
			return canciones
		urls = scraping_search(cancion)
		videos = transform_list_to_dict(urls)
		print(f" Opcion | Titulo")
		for key, item in videos.items():
			print(key, item[1])
		option = input("Elige opcion o buscar otra vez(S): ")
		try:
			option = int(option)
			video = pafy_video(videos[option][0])
			best = video.getbest().url
			x = {
				'opt': numeracion,
				'title': videos[option][1],
				'url': best
			}
			canciones.append(x)
			numeracion = numeracion + 1
		except:
			pass


if __name__ == '__main__':
	add_to_list('a', 'a')
	RUN = True
	search_s = True
	option = 'x'
	while RUN:
		if search_s:
			cancion = input("Introduce nombre de la cancion o Ver/selecionar lista (L) o descargar videos (D): ")
			search_s = False
		if cancion.upper() == 'EXIT':
			RUN = False
		if cancion.upper() == 'L':
			opt = input("LISTAS-> Reproducir(R), Ver(V), Crear(C), Añadir(A), Eliminar(D), Cancelar(E): ")
			if opt.upper() == 'R':
				lista = input("Nombre de la lista que quiere reproducir: ")
				canciones = add_to_list(lista)
				for c in canciones:
					stop = play_music(c[2])
			if opt.upper() == 'V':
				print(get_listas())
			if opt.upper() == 'C':
				canciones = search_song_for_list()
				name_list = input("Introduce el nombre de la lista: ")
				response = add_to_list(name_list, METHOD='PUT', data=canciones)
				print(response)
			if opt.upper() == 'A':
				name_list = input("En que lista quieres añadir canciones? ")
				canciones = search_song_for_list()
				response = add_to_list(name_list, METHOD='ADD', data=canciones)
				print(response)
			if opt.upper() == 'D':
				lista = input("Nombre de la lista que quiere eliminar: ")
				response = add_to_list(lista, METHOD='DELETE')
				if response:
					print(response)
			if opt.upper() == 'E':
				cancion = ''
		if use_api and cancion.upper() != 'L':
			videos_lst = youtube_search(cancion)
			videos = {videos_lst.index(i) + 1: i for i in videos_lst}
		if not(use_api) and cancion.upper() not in ['L', 'D']:
			urls_songs = scraping_search(cancion)
			videos = transform_list_to_dict(urls_songs)

		if cancion.upper() == 'D':
			search_s = input("Que quieres buscar? ")
			urls_songs = scraping_search(search_s)
			videos = transform_list_to_dict(urls_songs)
			print(f" Opcion | Titulo")
			for key, item in videos.items():
				print(key, item[1])
			option = input("Elige opcion, pase de pagina->(N) anterior pagina->(B) buscar otra vez->(S): ")
			try:
				option = int(option)
				video = videos[option][0]
				print(video)
				yt = pytube.YouTube(video)
				video = yt.streams.get_highest_resolution()
				print(video.title)
				video.download()
			except Exception as e:
				print(e)
				if option.upper() == 'EXIT':
					RUN = False
				elif option.upper() == 'N':
					pass
				elif option.upper() == 'B':
					pass
				elif option.upper() == 'S':
					search_s = True

		if cancion.upper() not in ['L', 'D', '']:
			print(f" Opcion | Titulo")
			for key, item in videos.items():
				print(key, item[1])
			option = input("Elige opcion, pase de pagina->(N) anterior pagina->(B) buscar otra cancion->(S): ")
			try:
				option = int(option)
				video = pafy_video(videos[option][0])
				best = video.getbest().url
				stop = play_music(best)
			except Exception as e:
				print(e)
				if option.upper() == 'EXIT':
					RUN = False
				elif option.upper() == 'N':
					pass
				elif option.upper() == 'B':
					pass
				elif option.upper() == 'S':
					search_s = True
		elif cancion.upper() == 'L':
			pass
		elif cancion == '':
			search_s = True
