import socket

class Socket:
    @staticmethod
    def create():
        addr = ("0.0.0.0", 81)
        print("socket created")
        return socket.create_server(addr)