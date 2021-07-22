import socket
import threading
import time


def send(user_name):
    while True:
        msg = input()
        data = user_name + ' > ' + msg
        cli_sock.send(data.encode('utf-8'))


def receive():
    while True:
        data = cli_sock.recv(1024).decode('utf-8')
        print('\t\t\t' + data)


def check_user_name(name):
    cli_sock.send(name.encode('utf-8'))
    data = cli_sock.recv(1024)
    return eval(data.decode('utf-8'))


if __name__ == "__main__":
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 12345

    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')

    while True:
        uname = input('Enter your name to enter the chat > ')
        is_allowed = check_user_name(uname)
        if is_allowed is False:
            print("You can't take this name")
        else:
            break

    thread_send = threading.Thread(target=send, args=[uname])
    thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()
