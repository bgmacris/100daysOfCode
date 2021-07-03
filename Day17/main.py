from tempfile import NamedTemporaryFile
import shutil


# Exemple chr(97), ord('a')

global abc
abc = "qwertasdfgzxcvbyuiophjklñnmç"
num = "1234567890"

def encrypt(content):
    data = ""
    for string in content:
        if string in abc:
            index = abc.index(string)
            if index == 26:
                index = 2
            elif index == 25:
                index = 1
            elif index == 24:
                index = 0
            else:
                index += 3
                
            data += abc[index]
        else:
            data += string  
    
    final_data = ""
    for string in data:
        if string in abc:
            final_data += f"%{ord(string)}%"
        else:
            final_data += string
        
    
    return final_data    


def decrypt(content):
    data = ""
    pos = 0
    num = 0
    data = []
    for i in content.split('%'):
        if i:
            data.append(i)
    
    real_data = ""
    for string in data:
        try:
            string = chr(int(string))
            if string in abc:
                index = abc.index(string)
                if index == 2:
                    index = 26
                elif index == 1:
                    index = 25
                elif index == 0:
                    index = 24
                else:
                    index = index - 3
                
                real_data += abc[index]
        except:
            real_data += str(string)

    return real_data

if __name__ == '__main__':
    text = open('text.txt', 'r')
    content = text.read()
    text.close()
    
    encrypt_data = encrypt(content.lower())
    print(encrypt_data, "\n")
    decrypt_data = decrypt(encrypt_data)
    print(decrypt_data)
    # text = open('text.txt', 'w')
    # text.write(encrypt(content))
            

        
