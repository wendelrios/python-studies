# cliente.py
import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("Digite uma mensagem ou tecle Enter para sair: ") 
 
tcpCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpCliente.connect((host, port))

while MESSAGE != '':
    tcpCliente.send(MESSAGE)     
    data = tcpCliente.recv(BUFFER_SIZE)
    print " Cliente recebeu a seguinte mensagem do servidor: ", data
    MESSAGE = raw_input("Cliente, digite uma mensagem ou tecle Enter para sair: ")

tcpCliente.close()