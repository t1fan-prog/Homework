import queue
import socket
import threading
from datetime import datetime


def accept_client():
    while True:
        # accept
        cli_sock, cli_add = ser_sock.accept()
        # добавлять на данном этапе
        CONNECTION_LIST.append(cli_sock)
        thread_client = threading.Thread(target=broadcast_usr, args=(cli_sock,))
        thread_client.start()
        # thread_client.join()


def check_or_create_name(name, cli_sock):
    if name not in NAMES.values():
        NAMES[cli_sock] = name
        new_user_alert = f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {name} connected to the chat'
        print(new_user_alert)
        send_msg(cli_sock, new_user_alert.encode('utf-8'))
        thread_write = threading.Thread(target=write_to_file, args=('history.txt', new_user_alert))
        thread_write.start()
        return True
    else:
        return False


def broadcast_usr(cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                data = data.decode('utf-8')
                if '>' not in data:  # Знак '>' есть во всех сообщения, кроме первого, в котором отправляется только имя
                    is_name = check_or_create_name(data, cli_sock)
                    cli_sock.send(f'{is_name}'.encode('utf-8'))
                else:
                    send_msg(cli_sock, f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {data}'.encode('utf-8'))
                    thread_write = threading.Thread(target=write_to_file, args=('history.txt', f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] {data}'))
                    thread_write.start()
                    print(data)
        except Exception as x:
            print(x)
            break


def send_msg(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock and client in NAMES:
            client.send(msg)


def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')


def read_from_file(filename, queue_for_file):
    try:
        with open(filename) as file:
            lines = file.readlines()
            chat = ''
            if len(lines) > 50:
                for i in lines[len(lines) - 50:]:
                    chat += f'{i}'
            else:
                for i in lines:
                    chat += f'{i}'
        queue_for_file.put(chat)
    except FileNotFoundError:
        with open('history.txt', 'w'):
            pass


if __name__ == "__main__":
    CONNECTION_LIST = []
    NAMES = {}
    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 12345
    ser_sock.bind((HOST, PORT))

    # listen
    ser_sock.listen(1)
    print('Chat server started on port : ' + str(PORT))

    queue_for_file = queue.Queue()

    thread_file = threading.Thread(target=read_from_file, args=('history.txt', queue_for_file))
    thread_file.start()
    thread_file.join()
    chat_history = queue_for_file.get()
    print(chat_history)

    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()

