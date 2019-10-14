# -*- coding: utf-8 -*-

from socket import *
import time

serverName = 'localhost'
clientPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
dataLen = 1000000

def request():
	filename = input('Nome da pagina: ')
	httpGet = "GET /" + filename + " HTTP/1.1\r\nHost: " + str(serverName) + ":" + str(clientPort) + "\r\n\r\n"

	print('Cliente se conectando ao balanceador')
	time.sleep(2)
	clientSocket.connect((serverName, clientPort))

	clientSocket.send(httpGet.encode())

	res_echo = clientSocket.recv(dataLen)
	time.sleep(2)
	print('Mensagem recebida do balanceador')
	time.sleep(2)
	print(res_echo.decode())
	clientSocket.close()
	print('Conexão fechada')

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