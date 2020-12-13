import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 

class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] Server socket iniciado em " + ip + ":" + str(port) 
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print "Mensagem recebida do cliente: ", data
            print "servico prestado pela thread ",self.ident
            MESSAGE = raw_input("digite uma mensagem de resposta para o cliente: ")
            if MESSAGE == '':
                break
            conn.send(MESSAGE)


TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print "Server python multithreading iniciado... Aguardando conexoes TCP..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 