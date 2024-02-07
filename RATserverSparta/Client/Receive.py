import socket
class Receive:
    @staticmethod
    def Receive(s: socket.socket, client_endpoint, bytes):
        while True:
            message = s.recv(bytes).decode("utf-8")
            print("Client: ", message, "from client:", client_endpoint)
            if message == "":
                print("Client disconnected")
                break