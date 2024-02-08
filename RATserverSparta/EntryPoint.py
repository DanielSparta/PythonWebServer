import socket
import threading

class Program:
    def __init__(self):
        print("Constructor created")

    def socket_create(self):
        socket = socket.socket_create(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        return socket.bind("0.0.0.0", 80)

    def socket_accept(self, s: socket.socket):
        while True:
            data = s.accept()

