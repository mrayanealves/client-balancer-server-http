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
	request = connectionSocket.recv(1024).decode()

	filename = request.split()[1]
	f = open(filename[1:], 'r')
	outputdata = f.read()

	print("Arquivo encontrado")
	headerLine = "HTTP/1.1 200 OK\r\n"
	connectionSocket.send(headerLine.encode())
	connectionSocket.send("\r\n".encode())

	# Sends the file
	for i in range(0, len(outputdata)):
		connectionSocket.send(outputdata[i].encode())
	connectionSocket.send("\r\n".encode())

	# Terminates the conection
	print("File sent.")
	connectionSocket.close()
	
	# encerra conexão com o balanceador
	connectionSocket.close()
	print('Conexão com o balanceador encerrada')