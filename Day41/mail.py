import imaplib
import email
import codecs
import time
import os


os.system('clear')
print(""" ███▄ ▄███▓    ▄▄▄          ██▓    ██▓    
▓██▒▀█▀ ██▒   ▒████▄       ▓██▒   ▓██▒    
▓██    ▓██░   ▒██  ▀█▄     ▒██▒   ▒██░    
▒██    ▒██    ░██▄▄▄▄██    ░██░   ▒██░    
▒██▒   ░██▒    ▓█   ▓██▒   ░██░   ░██████▒
░ ▒░   ░  ░    ▒▒   ▓▒█░   ░▓     ░ ▒░▓  ░
░  ░      ░     ▒   ▒▒ ░    ▒ ░   ░ ░ ▒  ░
░      ░        ░   ▒       ▒ ░     ░ ░   
       ░            ░  ░    ░         ░  ░
\n""")
imap_ssl_host = 'server-mail'
imap_port = 465
username = 'correo'
password = 'passwd'

try:
	imap = imaplib.IMAP4_SSL(imap_ssl_host)
	imap.login(username, password)
	imap.select('inbox')
	connected = True
except:
	print("No se ha podido establecer conexion. . .")
	connected = False

def main_mail():
	pass


while connected:
	status, data = imap.search(None, '(UNSEEN)')
	if status == 'OK':
		mail_ids = [block.split() for block in data][0]
		if mail_ids:
			for id in mail_ids:
				status, mail = imap.fetch(id, '(RFC822)')
				for response_part in mail:
					if isinstance(response_part, tuple):
						message = email.message_from_bytes(response_part[1])

						mail_from = message['from']
						mail_subject = message['subject']

						if message.is_multipart():
							print("Multipart")
							mail_content = ''
							for part in message.get_payload():
								print(part.get_content_type())
								if part.get_content_type() == 'text/plain':
									mail_content = mail_content + part.get_payload()
								if part.get_content_type() == 'text/html':
									content = bytes(part.get_payload(), encoding='utf-8')
									print(part['content-transfer-encoding'])
									if part['content-transfer-encoding'] == 'base64':
										content = codecs.decode(content, part['content-transfer-encoding'])
									mail_content = mail_content + str(content)
						else:
							mail_content = message.get_payload()

						print("#"*40)
						print(f"From: {mail_from}")
						print(f"Subject: {mail_subject}")
						print(f"Content: {mail_content}")
						print("#"*40)
	time.sleep(60)
