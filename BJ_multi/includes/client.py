import socket
import pygame
import subprocess


pygame.font.init()
pygame.init()
width = 800
height = 600
win = pygame.display.set_mode((width, height))  # création de la fenêtre
pygame.display.set_caption("Client")
pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1,0.0)


class Client():
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def init_client(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("[+] Client created")
        except socket.error as msg:
            print(f"[-] Error occured while attempting to create socket : {msg}")

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.IP, self.PORT))
        except socket.error as msg:
            print(f"[-] Socket connection error: {msg}")

    def send_to_client(self):
        self.message = ""
        self.data = ""
        while self.message != 'exit':
            self.message = input(">")
            self.client_socket.sendall(self.message.encode("utf-8"))
            self.data = self.client_socket.recv(2048)
            print(self.data.decode())

    def execute(self):
        self.init_client()
        self.connect_to_server()
        self.send_to_client()

    oui = True
    clock = pygame.time.Clock()
    yellow_box = pygame.image.load("../img/yellow_box_179_120.png").convert_alpha()
    bj_banner = pygame.image.load("../img/bj_banner_yellow2.png").convert_alpha()

    while oui:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oui = False
        win.fill((34, 139, 34))
        x_pos = int((800, 600)[0] * 0.12)
        y_pos = (800, 600)[1] - 240
        win.blit(yellow_box, (x_pos, y_pos))
        x_pos = int(((800, 600)[0] - (bj_banner).get_width()) / 2)
        y_pos = (800, 600)[1] - 500
        win.blit(bj_banner, (x_pos, y_pos))
        pygame.display.flip()
        clock.tick(60)



client = Client("0.0.0.0", 1234)
client.execute()
