import socket
from caesar import caesar_cipher

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 65433)

sock.bind(server_address)

message = ''
offset = ''
lang = ''

i = 0
result = 'test'
for _ in range(3):
    data, addr = sock.recvfrom(4096)
    if i == 0:
        message = data.decode('utf-8')
    elif i == 1:
        offset = data.decode('utf-8')
    elif i == 2:
        lang = data.decode('utf-8')
        test = caesar_cipher(message, int(offset), lang)
        sock.sendto(test.encode('utf-8'), addr)
    i += 1


print(message, offset, lang)
