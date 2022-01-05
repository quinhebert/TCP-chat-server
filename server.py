import socket
import threading

HOST = '127.0.0.1'
PORT = 9090
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []
messageStorage = {}

#broadcast to all of the clients
def broadcast(message, sendTo):
    print("Send To: " + sendTo)
    if sendTo == 'everyone':
        for client in clients:
            client.send(message)
    else:
        if sendTo.encode(FORMAT) in nicknames:
            for name in nicknames:
                decodedName = name.decode(FORMAT)
                if decodedName == sendTo:
                    clients[nicknames.index(name)].send(message)
            print(nicknames)
            print(messageStorage)
        else:
            #save message for when user reconnects
            messageStorage[sendTo] = message





#handle the individual connections from the client
def handle(client):
    while True:
        try:
            #if there is a message -> broadcast it to the client
            message = client.recv(1024)
            #decipher if it is client specific or group
            decodedMessage = message.decode(FORMAT)
            if "::" in decodedMessage:
                sendToName = decodedMessage.partition(":")[0]
                sendToName = sendToName.partition(">")[2]
                broadcast(decodedMessage.encode(FORMAT), sendToName)
            elif message:
                broadcast(message, 'everyone')
        except Exception:
            #error handling
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} has left the chat!'.encode('utf-8'), 'everyone')
            break
        




#receive the connections from the client (main function in the main thread)
def receive():
    while True:
        #accept new connections - accept returns client and server addresses
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        #ask the client for a nickname for the user
        client.send("nickname".encode(FORMAT))
        nickname = client.recv(1024)
        nicknames.append(nickname)

        #add client to the clients list
        clients.append(client)

        print("Name of the client is " + str(nickname.decode(FORMAT)))
        #let everyone know who has connected
        broadcast(f"{nickname.decode(FORMAT)} has joined the chat!\n".encode(FORMAT), 'everyone')
        #let the client know they are connected
        client.send("Connected to the server\n".encode(FORMAT))

        #send client the missed messages
        for messages in messageStorage:
            if messages.encode(FORMAT) == nickname:
                print(messageStorage[nickname.decode(FORMAT)])
                broadcast(messageStorage[nickname.decode(FORMAT)], nickname.decode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


#START
#start the server by running main function
print("Server Starting...")
receive()