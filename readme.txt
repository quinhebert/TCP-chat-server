Open a new terminal at the project folder and start the server using the following command:
'python3 server.py'
![Starting Server](https://github.com/quinhebert/TCP-chat-server/blob/master/images/start%20server.png?raw=true)

Start a client by opening another terminal at the folder and use the following command:
'python3 client.py'

Starting multiple clients and giving them names:
![Starting Client 1 (Quin)](https://github.com/quinhebert/TCP-chat-server/blob/master/images/start%20client1.png?raw=true)
![Starting Client 2 (Devin)](https://github.com/quinhebert/TCP-chat-server/blob/master/images/start%20client2.png?raw=true)

You can interact with the client by entering a name and then simply type your message and press enter.
If you type a message and press enter it will be broadcasted to everyone (Alli sends a message to everyone):
![Alli sends a message](https://github.com/quinhebert/TCP-chat-server/blob/master/images/Alli%20Sends.png?raw=true)

You can send a direct message by typing '<username>::<message>', so if I wanted to send a message to a user with the name Bob,
I would type 'Bob::this is my message'; This message will be broadcasted from the server only to Bob.
Devin sends a direct message to Alli:
![Devin sends a direct message](https://github.com/quinhebert/TCP-chat-server/blob/master/images/devin%20sends%20direct.png?raw=true)

Alli receives the direct message from Devin:
![Alli receives a direct message](https://github.com/quinhebert/TCP-chat-server/blob/master/images/alli%20receives%20direct.png?raw=true)

Quin is unable to see the message because it was sent as a direct message:
![Quin can't see the direct message](https://github.com/quinhebert/TCP-chat-server/blob/master/images/quin%20cant%20see%20direct.png?raw=true)
