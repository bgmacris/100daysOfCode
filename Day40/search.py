import sys
import re, requests, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from apiclient.discovery import build
from apiclient.errors import HttpError
import pafy
import vlc

API_KEY = 'AIzaSyAQeYyxjlPmmqEtakeOdQ6fvhzBMYVuuUk'
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


def play_music(url):
	Instance = vlc.Instance('-I dummy --no-video')
	#Instance = vlc.Instance()
	player = Instance.media_player_new()
	Media = Instance.media_new(str(url))
	Media.get_mrl()
	player.set_media(Media)
	player.play()
	print("La musica esta sonando. . .")
	while True:
		option = input("Stop -> (S), Pause -> (P), Play -> (R)")
		if option.upper() == 'S':
			print("Se ha parado la musica")
			player.stop()
			break
		elif option.upper() == 'P':
			print("Se ha pausado la musica")
			player.pause()
		elif option.upper() == 'R':
			print("Se reproduce la musica")
			player.play()
	player.stop()


RUN = True
search_s = True
option = 'x'
while RUN:
	if search_s:
		cancion = input("Introduce nombre de la cancion: ")
		search_s = False
	if cancion.upper() == 'EXIT':
		RUN = False

	if use_api:
		videos_lst = youtube_search(cancion)
		videos = {videos_lst.index(i) + 1: i for i in videos_lst}
	if not(use_api):
		query_string = urllib.parse.urlencode({"search_query": cancion})
		formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
		search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
		urls_songs = [f"https://www.youtube.com/watch?v={id}" for id in search_results]
		urls = []
		for url in urls_songs[:5]:
			response = requests.get(url, cookies={'CONSENT': 'YES+1'})
			vid = pafy.new(url)
			title = vid.title
			urls.append((url, title))
		videos = {urls.index(i) + 1: i for i in urls}

	print(f" Opcion | Titulo")
	for key, item in videos.items():
		print(key, item[1])
	option = input("Elige opcion, pase de pagina->(N) anterior pagina->(B) buscar otra cancion->(S): ")
	try:
		option = int(option)
		video = pafy_video(videos[option][0])
		best = video.getbest().url
		play_music(best)
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

