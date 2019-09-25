from socket import *

serverPort = 12001

# cria socket do servidor
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('O servidor 0 está pronto para ouvir')

while 1:
	print('Ouvindo...')

	# socket do servidor aceita conexão do balanceador
	connectionSocket, addr = serverSocket.accept()
	print('Conectado ao balanceador:', addr)

	# recebe mensagem do balanceador
	sentence = connectionSocket.recv(1024)

	# converte a mensagem para letras maiusculas
	capitalizedSentence = sentence.upper()
	print('Nova mensagem a ser enviada: ', capitalizedSentence)

	# envia de volta a mensagem modificada para o balanceador
	connectionSocket.send(capitalizedSentence)
	
	# encerra conexão com o balanceador
	connectionSocket.close()
	print('Conexão com o balanceador encerrada')