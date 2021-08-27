import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 65433)

sock.bind(server_address)


while True:
    data, addr = sock.recvfrom(4096)
    message = data.decode('utf-8')
    print(message)
    sock.sendto('Hello from server'.encode('utf-8'), addr)
