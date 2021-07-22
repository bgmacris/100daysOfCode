import nmap

nm = nmap.PortScanner()

def devices_connected(host=None):
    if not(host):
        return "No host declared"
    result = nm.scan(hosts=host, arguments='-sP')
    hosts_list = []
    if result:
        for i in result['scan']:
            if i != None:
                hosts_list.append(i)
        up_host = len(hosts_list)
        return {'hosts': hosts_list, 'info': f"Up Host {up_host}"}
    return False

def scan_random_targets(num_host):
    result = nm.scan(hosts='192.168.0.1', arguments=f"-iR {num_host}")
    uphosts = result['nmap']['scanstats']['uphosts']
    list_hosts = [host for host in result['scan']]
    return {'up Hosts': uphosts, 'List Host': list_hosts}

def os_info(host):
    nm.scan(hosts=host, arguments='-oX')
#    print(nmap.nm.get_nmap_last_output())


#print(devices_connected("192.168.0.1/24"))
#print(scan_random_targets(2))
print(os_info('192.168.0.110'))
