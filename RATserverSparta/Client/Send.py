import socket
class Send:
    @staticmethod
    def send(message: socket.socket, data):
        data.send(message.encode('utf-8'))