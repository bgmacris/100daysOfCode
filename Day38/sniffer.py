import socket
from parsepacket import ethernet_head
from parsepacket import ipv4_head

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
	raw_data, addr = s.recvfrom(65565)
	eth = ethernet_head(raw_data)
	ipv4 = ipv4_head(eth[3])
	print(f"MAC_dest: {eth[0]} MAC_source: {eth[1]} Protocol: {eth[2]}")
	print(ipv4)
