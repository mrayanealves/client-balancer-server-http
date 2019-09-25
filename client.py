from socket import *
serverName = 'localhost'
clientPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
# conexão com o balanceador
clientSocket.connect((serverName,clientPort))
sentence = input('Insira uma sentença minuscula: ')
print('Aguardando resposta do servidor')
# envia sentença minuscula para o balanceador, que irá enviar para o servidor
clientSocket.send(sentence.encode())
# recebe sentença maiuscula do balanceador
modifiedSentence = clientSocket.recv(1024)
print ('Do servidor:', modifiedSentence.decode())
clientSocket.close()