import os

def scan_ip(router):
    router = router.split('.')
    print(router)
    up_ips = []
    down_ips = []
    for i in range(1,255):
        router[-1] = str(i)
        ip = '.'.join(router)
        
        response = os.system(f"ping {ip}")
        if response == 0:
            up_ips.append(ip)
        else:
            down_ips.append(ip)
    return up_ips, down_ips

up_ips, down_ips = scan_ip('192.168.0.1')
print(f"Up Ip's: {up_ips}")
print(f"Down Ip's: {down_ips}")
