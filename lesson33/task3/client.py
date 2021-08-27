import socket
import time

server_address = ('localhost', 65434)


def client(server_address, var):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(server_address)
        message = f'Hello, dude, this is {var} connection'.encode('utf-8')
        s.sendto(message, server_address)
        data, addr = s.recvfrom(1024)
        print('Received', f'"{data.decode("utf-8")}"')


for i in range(1, 9):
    client(server_address, i)
