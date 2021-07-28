import socket

server_address = ('localhost', 65434)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(server_address)
    message = 'Hello, dude'.encode('utf-8')
    s.sendto(message, server_address)
    data, addr = s.recvfrom(4096)

print('Received', f'"{data.decode("utf-8")}"')
