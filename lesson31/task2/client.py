import socket

server_address = ('localhost', 65433)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(server_address)
    message = 'Здарова'.encode('utf-8')
    offset = '3'.encode('utf-8')
    lang = 'ru'.encode('utf-8')
    s.sendto(message, server_address)
    s.sendto(offset, server_address)
    s.sendto(lang, server_address)
    data, addr = s.recvfrom(4096)

print('Закодированное сообщение:', data.decode('utf-8'))
