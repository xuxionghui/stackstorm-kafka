import struct
import socket
import random
from st2common.runners.base_action import Action

class IpRandomAction(Action):
    def run(self):
        print(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
