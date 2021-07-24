import struct
import sys
import socket

def get_mac_addr(bytes_addr):
	bytes_str = map('{:02x}'.format, bytes_addr)
	mac_addr = ':'.join(bytes_str).upper()
	return mac_addr

def ipv4(addr):
	return '.'.join(map(str, addr))

def ethernet_head(raw_data):
	dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])
	print(dest)
	dest_mac = get_mac_addr(dest)
	src_mac = get_mac_addr(src)
	proto = socket.htons(prototype)
	data = raw_data[14:]
	return dest_mac, src_mac, proto, data

def ipv4_head(raw_data):
	ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
	return ttl, proto, ipv4(src), ipv4(target)
