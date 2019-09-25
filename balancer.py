from socket import *

# Exemplo de comando para matar o servidor
# $ ps -fA | grep python
#501 81211 12368   0  10:11PM ttys000    0:03.12  python -m SimpleHTTPServer
#$ kill 81211
serverName = 'localhost'
clientPort = 12000
# socket que faz a conexão com algum cliente (funciona como um servidor)
app_client_Socket = socket(AF_INET,SOCK_STREAM)
app_client_Socket.bind(('',clientPort))
app_client_Socket.listen(1)
print('O app está pronto para receber')
while 1:
	print('Ouvindo...')
	# aceita conexão de um cliente
	connectionSocket, addr = app_client_Socket.accept()
	print('Endereço do cliente: ', addr)
	# recebe mensagem do cliente
	sentence = connectionSocket.recv(1024)
	print('Mensagem recebida do cliente: ', sentence)

	print('Encaminhando para o servidor')
	serverPort = 12001
	# cria socket para se comunicar com o servidor (funciona como um cliente)
	app_server_Socket = socket(AF_INET, SOCK_STREAM)
	app_server_Socket.connect((serverName,serverPort))
	# envia mensagem para o servidor
	app_server_Socket.send(sentence)

	#recebe mensagem do servidor
	modifiedSentence = app_server_Socket.recv(1024)
	print('Mensagem recebida do servidor')
	# encerra conexão com o servidor
	app_server_Socket.close()
	print('Conexão com o servidor encerrada')
	print('Enviando mensagem para o cliente')
	# envia mensagem para o cliente
	connectionSocket.send(modifiedSentence)
	# encerra conexão com um cliente
	connectionSocket.close()
	print('Conexão com o cliente encerrada')