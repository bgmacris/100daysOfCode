import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
while True:
    packet = s.recvfrom(2048)
    
    eth_header = struct.unpack("!6s6s2s", packet[0][:14])
    print(f"Source MAC: {binascii.hexlify(eth_header[1])}")
    
    ip_header = struct.unpack("!12s4s4s", packet[0][14:34])
    print(f"Source IP: {socket.inet_ntoa(ip_header[1])}")
