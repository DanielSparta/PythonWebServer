import socket
import threading
import Client.Client
class Socket:
    @staticmethod
    def accept(s: socket.socket):
        client_socket = s.accept()
        client_class = Client.Client.client()
        print("client connected")
        threading.Thread(target=client_class.test, args=(client_socket,)).start()
        print("client connected after thread")