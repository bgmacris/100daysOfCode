import pafy
import moviepy.editor as mp
import telebot
import os

API_KEY = 'API KEY'
bot = telebot.TeleBot(API_KEY)

global MUSIC_PATH
MUSIC_PATH = os.path.join(os.getcwd(), 'music/')

def download_mp3(url):
	video = pafy.new(url)
	audio = video.getbest(preftype="mp4")
	print(video.title)
	audio.download()

	get_audio = mp.VideoFileClip(rf"{video.title}.mp4")
	get_audio.audio.write_audiofile(rf"{MUSIC_PATH}{video.title}.mp3")
	os.system(f'rm *.mp4')
	return video.title

@bot.message_handler(commands=['mp3'])
def mp3(message):
	URL = message.text.replace('/mp3 ', '')
	audio = download_mp3(URL)
	bot.send_audio(chat_id=message.chat.id, audio=open(f'{MUSIC_PATH}{audio}.mp3', 'rb'))

bot.polling()
