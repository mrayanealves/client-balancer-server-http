from socket import *


def round_robin(cont, servers):
	if(cont == 0):
		cont += 1
		return (cont, servers[0])
	if(cont == 1):
		cont += 1
		return (cont, servers[1])
	if(cont == 2):
		cont = 0
		return (cont, servers[2])


# Exemplo de comando para matar o servidor
# $ ps -fA | grep python
#501 81211 12368   0  10:11PM ttys000    0:03.12  python -m SimpleHTTPServer
#$ kill 81211
serverName = 'localhost'
clientPort = 12000

# lista de portas dos servidores
servers = [12001, 12002, 12003]
cont = 0

# socket que faz a conexão com algum cliente (funciona como um servidor)
app_client_Socket = socket(AF_INET,SOCK_STREAM)
app_client_Socket.bind(('',clientPort))
app_client_Socket.listen(1)

while 1:
	print('O balanceador de carga está ouvindo')

	# aceita conexão de um cliente
	connectionSocket, addr = app_client_Socket.accept()
	print('Endereço do cliente: ', addr)

	# recebe mensagem do cliente
	sentence = connectionSocket.recv(1024)
	print('Mensagem recebida do cliente: ', sentence.decode())
	
	print('Encaminhando para o servidor')

	# seleciona o servidor de acordo com a função round robin
	cont, serverPort = round_robin(cont, servers)

	# cria socket para se comunicar com o servidor (funciona como um cliente)
	app_server_Socket = socket(AF_INET, SOCK_STREAM)
	app_server_Socket.connect((serverName,serverPort))

	# envia mensagem para o servidor
	app_server_Socket.send(sentence)

	data = ""
	while True:
		newData = app_server_Socket.recv(1024).decode()
		data += newData
		if (len(newData) == 0):
			break

	print('Dados recebidos do servidor')

	# encerra conexão com o servidor
	app_server_Socket.close()
	print('Conexão com o servidor encerrada')
	print('Enviando mensagem para o cliente')

	# envia mensagem para o cliente
	connectionSocket.send(data.encode())
	
	# encerra conexão com um cliente
	connectionSocket.close()
	print('Conexão com o cliente encerrada')