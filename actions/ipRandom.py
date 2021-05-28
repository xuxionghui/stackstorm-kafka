import struct
import socket
import random


class IpRandomAction(Action):
    def run(self):
        print(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))