from socket import *

serverName = 'localhost'
clientPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
dataLen = 1000000

def request():
    get = "GET / HTTP/1.1\r\nHost: " + str(serverName) + ":" + str(clientPort) + "\r\n\r\n"
    
    clientSocket.connect((serverName,clientPort))

    clientSocket.send(get.encode())

    res_echo = clientSocket.recv(dataLen)
    print(res_echo.decode())
    clientSocket.close()

request()

# # conexão com o balanceador
# clientSocket.connect((serverName,clientPort))
# sentence = input('Insira uma sentença minuscula: ')
# print('Aguardando resposta do servidor')

# # envia sentença minuscula para o balanceador, que irá enviar para o servidor
# clientSocket.send(sentence.encode())

# # recebe sentença maiuscula do balanceador
# modifiedSentence = clientSocket.recv(1024)
# print ('Do servidor:', modifiedSentence.decode())
# clientSocket.close()