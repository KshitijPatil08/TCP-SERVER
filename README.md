﻿# TCP-SERVER
 Server.py
 
 import socket:
Purpose: Imports the socket library to create and manage network connections.

2. serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM):
socket.socket(): Creates a new socket object for network communication.
socket.AF_INET: Specifies the address family, which is IPv4.
socket.SOCK_STREAM: Specifies the type of socket, which is a stream socket used for TCP communication.

4. host = socket.gethostbyname('localhost'):
socket.gethostbyname(): Resolves the hostname 'localhost' into its corresponding IP address.
host: The resolved IP address is stored in the variable host.

5. port = 1024:
Purpose: Assigns the port number 1024 to the port variable. Ports between 0 and 1023 are privileged, so 1024 is a commonly used port number for non-administrative use.

6. serversocket.bind(("x.xxx.xxx.xxx", port)):
serversocket.bind(): Binds the socket to an IP address and port.
("x.xxx.xxx.xxx", port): A tuple specifying the IP address and port number where the server will listen for connections.
The IP address x.xxx.xxx.xxx is a placeholder and must be replaced with a valid IP address, such as '0.0.0.0' (bind to all available interfaces) or '127.0.0.1' (bind to localhost).

7. serversocket.listen(3):
Purpose: Puts the server socket into listening mode, allowing it to accept incoming connections.
3: Specifies the maximum number of queued connections before refusing new ones.

8. while True:
Purpose: Keeps the server running in an infinite loop, so it can continuously accept new client connections.

9. clientsocket, addr = serversocket.accept():
serversocket.accept(): Waits for an incoming connection and returns:
clientsocket: A new socket object for communication with the connected client.
addr: The address of the connected client (IP and port).

10. print("Got a connection from %s" % str(addr)):
Purpose: Logs the IP address and port of the client that just connected.

11. message = "hello! Thank you for connecting to the server" + '\r\n' :
Purpose: Creates a string message to send to the client, welcoming them to the server.
\r\n: Adds a carriage return and newline to indicate the end of the message.

12. clientsocket.send(message.encode('ascii')):
clientsocket.send(): Sends the encoded message to the client.
message.encode('ascii'): Converts the string message into bytes using ASCII encoding, as sockets can only send byte data.

13. clientsocket.close() :
Purpose: Closes the connection with the client, freeing up resources.

Client.py

host = socket.gethostbyname()
socket.gethostbyname: This function resolves a hostname (e.g., www.example.com) into an IP address. However, this line is incorrect because host is assigned the function reference, not the resolved hostname. The correct usage would be, for example:

host = socket.gethostbyname('hostname')
port = 1024
port: Specifies the port number to which the client will connect. In this case, 1024 is the port. Port numbers below 1024 are reserved for privileged or well-known services and usually require administrator privileges to bind.

clientsocket.connect(('host', port))
clientsocket.connect: Initiates a connection to the server specified by the host and port.
('host', port): A tuple containing the hostname (host) and port number (port). However, 'host' as a string literal is incorrect; it should be replaced with the actual hostname or IP address, like '127.0.0.1'.

message = clientsocket.recv(1024)
clientsocket.recv(1024): Receives data from the server, up to 1024 bytes. The 1024 parameter specifies the maximum amount of data to receive at once.

clientsocket.close()
clientsocket.close(): Closes the socket connection to the server, releasing any resources associated with it.

print(message.decode('ascii'))
message.decode('ascii'): Decodes the received byte data (message) into a string using ASCII encoding.
print: Outputs the decoded message to the console.
