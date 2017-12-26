#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
port_number = 6784
serverSocket.bind(('', port_number))
serverSocket.listen(1)
while True:
    #Establish the connection
    print ('Ready to serve....')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
       # print ("\n outputdata:", outputdata)
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK \r\n\r\n'.encode())
        #connectionSocket.send(outputdata.encode())
        
        #Send the content of the requested file to the client
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for the file not found
        #print ('404 Not Found')
        connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>".encode())
    connectionSocket.close()
serverSocket.close()