'''
Este servidor irá testar se um número é par ou ímpar
'''

import socket as s

def verificar(valorAReceber):
    resto = valorAReceber % 2

    if(resto == 0):
        print("Número é par")
    else:
        print("É ímpar!")

serverPort = 8000
serverIP = '127.0.0.1'

serverSocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))
print("Server listening...")

while True: 
    valorAReceber, address = s.socket.recvfrom(serverSocket, 1024)
    print("The message ", valorAReceber.decode(), " was received.")
    valor = int(valorAReceber.decode())
    verificar(valor)
