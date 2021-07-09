import concurrent.futures
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 65434)

sock.bind(server_address)

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(sock.recvfrom, 1024) for i in range(64)]
        for f in concurrent.futures.as_completed(results):
            data, addr = f.result()
            message = data.decode('utf-8')
            print(message, addr)
            sock.sendto(f'{message}'.encode('utf-8'), addr)
