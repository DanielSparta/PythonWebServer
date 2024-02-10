import socket
import threading
from encodings.utf_8 import encode


class Program:
    def __init__(self):
        print("Constructor created")

    def socket_create(self):
        socket = socket.socket_create(AF_INET, SOCK_STREAM, IPPROTO_TCP)
        return socket.bind("0.0.0.0", 80)
    def socket_accept(self, s: socket.socket):
        while True:
            data = s.accept()

    def socket_send(self, s: socket.socket, message):
        s.socket_send(encode("utf-8", message))

    def socket_recv(self, s: socket.socket):
        while True:
            data = s.recv(1000).decode("utf-8")