import socket
import threading


def on_new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"[+]A new connection was made from IP: {ip}, and port: {port}")
    while True:
        msg = client.recv(2048)
        if msg.decode() == "exit":
            break
        print(f"{ip}>{msg.decode()}")
        reply = f"{msg.decode()}"
        client.sendall(reply.encode('utf-8'))
    print(f"The client from ip: {ip}, and port: {port}, has gracefully diconnected!")


class ServerMultiThreading():
    def __init__(self, PORT, IP):
        self.PORT = PORT
        self.IP = IP

    def creating_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[+] Server created")
        except socket.error as msg:
            print(f"[-] Error occured while attempting to create socket : {msg}")

    def binding_to_server(self, PORT, IP):
        try:
            print(f"[+] Binding to port : {self.PORT}")
            self.server_socket.bind((self.IP, self.PORT))
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except socket.error as msg:
            print(f"[-] An Error occured while attempting to bind : {msg}")

    def accepting_to_server(self):
        while True:
            self.server_socket.listen(7)
            self.conn, self.adress = self.server_socket.accept()
            self.new_thread = threading._start_new_thread(on_new_client, (self.conn, self.adress))
            self.threads.append(self.new_thread)

    def launch_server(self):
        self.threads = []
        self.creating_server()
        self.binding_to_server(self.PORT, self.IP)
        self.accepting_to_server()


server = ServerMultiThreading(1234, "0.0.0.0")
server.launch_server()
