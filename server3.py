# -*- coding: utf-8 -*-

from socket import *
import os.path
import datetime, time

serverIP = 'localhost' # local ip address
serverPort = 12003
dataLen = 1000000

def get_modDate(s):
    date = ""
    list = []
    temp = ""
    bool = False
    for i in s:
        if i == '\n':
            temp += i
            list += [temp]
            temp = ""
        else:
            temp += i

    for i in list[2]:
        if bool == True:
            date += i
        elif i == ' ':
            bool = True
        else:
            continue
    return date

# cria socket do servidor
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)


#loop forever
while True:
    print('O servidor 3 está ouvindo...')
    #socket servidor aceita conexao com balanceador
    connectionSocket, addr = serverSocket.accept()
    print('Conectado ao balanceador:', addr)
    time.sleep(2)

    res = ""

    #get todays date
    t1 = datetime.datetime.now(datetime.timezone.utc)
    date = t1.strftime("%a, %d %b %Y %H:%M:%S %Z")
    print('Data: ', date)
    time.sleep(2)

    #read bytes from socket
    data = connectionSocket.recv(dataLen).decode()
    print("Dados do cliente: \n" + data)
    time.sleep(2)
    # get the absolute path of the directory
    directory = os.getcwd()

    # get name of the file
    name = data.split()[1]
    name = name[1:]

    # adds filename on the path
    fname = os.path.join(directory, name)

    #if file doesn't exist, end immediatly
    if os.path.isfile(fname) != True:
        res += "HTTP/1.1 404 NOT FOUND\r\n"+"Date: " + date + "\r\n"
        connectionSocket.send(res.encode())
        connectionSocket.close()
        print('Conexao fechada')
        continue

    cli_modDate = get_modDate(data)

    #server file mod date
    secs = os.path.getmtime(fname)
    tup = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", tup)
    # Check if the file exists then GET if the the last modtime == previous modtime sent by client
    if os.path.isfile(fname) & (cli_modDate != last_mod_time):
        html_code = ""
        res += "HTTP/1.1 200 OK\r\n"+"Date: " + date + "\r\n"
        res += "Last-Modified: " + last_mod_time

        f_handle = open(name, 'r')
        for line in f_handle:
            html_code += line
        f_handle.close()
        res += "Content-Length: " + str(len(html_code)) + "\r\n"
        res += "Content-Type: text/html; charsetUTF-8\r\n\r\n"
        res += html_code

    # Conditional GET
    if os.path.isfile(fname) & (cli_modDate == last_mod_time):
        html_code = ""
        res += "HTTP/1.1 304 Not Modified\r\n"+"Date: " + date + "\r\n\r\n"

    print("Enviando resposta ao balanceador")
    time.sleep(2)
    connectionSocket.send(res.encode())
    connectionSocket.close()
    print('Conexão fechada')