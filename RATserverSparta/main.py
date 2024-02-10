import threading
import socket





class ClientsManager:
    def __init__(self, ip_listen, port_listen):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_listen = ip_listen
        self.port_listen = port_listen
        self.server_address = (ip_listen, port_listen)
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(5)
        self.clients_list = []
        pass

    def run(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.clients_list.append((client_socket, client_address))
            print(f"New connection from {client_address}. Total connected clients: {len(self.clients_list)}")



def main():
    clients_manager = ClientsManager('0.0.0.0', 81)
    thread = threading.Thread(target=clients_manager.run)
    thread.start()
    while True:
        command = input("command")
        client_index = input("index")
        clients_manager.clients_list[client_index].send(command.encode())

if __name__ == "__main__":
    main()
else:
    print("This program doesn't support importing")
