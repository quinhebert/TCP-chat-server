import socket
import threading

HOST = '127.0.0.1'
PORT = 9090
FORMAT = 'utf-8'


nickname = input('What is your name? ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'nickname':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break


def send():
    while True:
        message = "<" + nickname + ">" + input('')
        client.send(message.encode(FORMAT))



receiveThread = threading.Thread(target=receive)
receiveThread.start()

sendThread = threading.Thread(target=send)
sendThread.start()