'''
Week 3: Networks and Sockets

Transport Control Protocol
- built on top of IP (Internet Protocol)
- Assumes IP might lose some data - stores and retransmits data if it seems to be lost
- handles 'flow control' using a transmit window
- provides a nice reliable pipe

transport layer
- first layer
- end to end

TCP Connections / Sockets
- endpoint of a bidirectional INTER-PROCESS communication flow accross and Internet Protocol-based computer network such as the Internet

Ex: Process <-- Internet --> Process

TCP Port Numbers
- a port is an applications-specific or process-specific software communication endpoint
- it allows multiple networked applications to coexist on the same server
- ther is a list of well-known TCP port numbers

Application Protocol
-

HTTP - Hypetext Transfer Protocol
- the dominant application layer protocol on the Internet
- invented for the web; to retrieve HTML, images, documents, etc
- Basic concept: make a connection > request a document > retrieve the document > close the connection
- set of tules to allow browsers to retrieve web documents from servers over the internet

URL - uniform resource locators

Getting data from the server

'''
# How to connect using Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True :
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysock.close()
