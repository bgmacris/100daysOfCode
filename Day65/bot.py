import os
import telebot
from cryptography.fernet import Fernet

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# GLOBAL VARIABLES
global ENCRYPT, DECRYPT, __KEY__
ENCRYPT = False
DECRYPT = False
__KEY__ = None

def generar_key():
	key = Fernet.generate_key()
	return key

def encrypt_data(data):
	key = generar_key()
	f = Fernet(key)
	encrypt_text = f.encrypt(data).decode()
	return key, encrypt_text

def decrypt_data(key, data):
	key = key.encode()
	data = data.encode()
	print("DECRYPTT", data)
	f = Fernet(key)
	decrypt_data = f.decrypt(data).decode()
	return decrypt_data

def listener(messages):
	global ENCRYPT, DECRYPT
	for m in messages:
		if m.content_type == 'text':
			if ENCRYPT:
				key, encrypt_text = encrypt_data(m.text.encode())
				msg = f"MENSAGE ENCRIPTADO\n{encrypt_text}\nCLAVE\n{key.decode()}"
				bot.reply_to(m, msg)
				ENCRYPT = False
			elif DECRYPT and __KEY__ != None:
				decrypt_text = decrypt_data(__KEY__, m.text)
				msg = f"MENSAGE DECRIPTADO\n{decrypt_text}"
				bot.reply_to(m, msg)
				DECRYPT = False
bot.set_update_listener(listener)

@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, "hahaha no.")

@bot.message_handler(commands=['encrypt'])
def why(message):
	global ENCRYPT
	bot.reply_to(message, "Envia el mensaje que quieres encriptar")
	ENCRYPT = True

@bot.message_handler(commands=['decrypt'])
def answer(message):
	global DECRYPT
	DECRYPT = True
	bot.reply_to(message, "/key [clave] - para actualizar la clave")

@bot.message_handler(commands=['key'])
def anser(message):
	global __KEY__
	__KEY__ = message.text.replace('/key ', '')
	print(__KEY__)
	bot.reply_to(message, "La clave a sido configurada, introduce texto que desencriptar.")

bot.polling()
