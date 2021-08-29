import os
from datetime import datetime

def ping(list_host):
    DateTime = datetime.today()
    Date = DateTime.strftime('%d/%m/%Y   %H H:%M min')
    f = open('C:\\Users\\Administrator\\Desktop\\Python\\ping\\list_host.txt', 'a+')
    f.write(f"Fecha/hora: {Date}\n"+ '-'*35+"\n")
    for host in list_host:
        result = os.popen(f'ping {host}').read()
        if 'Lost = 0' in result:
            print(host, 'OK')
            f.write(f'{host}: {list_host[host]} -> OK\n')
        else:
            print(host, 'ERROR')
            f.write(f'{host}: {list_host[host]} -> ERROR\n')
    f.write("\n\n")
    f.close()

list_host = {'10.240.143.129': 'Router',
             '10.240.143.130': 'RSA Card',
             '10.240.143.142': 'Igel',
             '10.240.143.134': 'global-iss',
             '10.240.143.135': 'micros-pos',
             '10.240.143.136': 'micros-posdb',
             '10.240.143.137': 'micros-posmob',
             '10.240.143.138': 'global-util'
             }
ping(list_host)