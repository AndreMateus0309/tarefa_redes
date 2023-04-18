from socket import *

serverName = "127.0.0.1"
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
numero = "123"
clientSocket.send(numero.encode())
print("Número enviado ao servidor UDP: " + numero)
clientSocket.close()