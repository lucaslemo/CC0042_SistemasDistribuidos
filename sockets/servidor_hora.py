import socket
import threading
from datetime import datetime


def conexao_cliente_tcp(client, address):
    print('Conexão estabelecida com %s %s' % address)
    while (True):    
        data = client.recv(2048)
        mensagem = data.decode()
        if (mensagem != '0'):
            print('Respondendo mensagem para %s %s' % address)
            time = datetime.now()
            timeString = time.strftime('%H:%M:%S')
            client.sendall(timeString.encode('utf-8'))
        else:
            print('Fechando conexão com %s %s' % address, end='\n\n')
            client.sendall('0'.encode())
            break
    client.close()


def conexao_cliente_udp(sock, client, address):
    print('Requisição recebida de %s %s' % address)
    time = datetime.now()
    timeString = time.strftime('%H:%M:%S')
    sock.sendto(timeString.encode('utf-8'), address)


def main_TCP(server_address):

    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print ("Iniciando servidor TCP na porta %s %s\n" % server_address)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        client, address = sock.accept()
        conexao = threading.Thread(target=conexao_cliente_tcp,args=(client, address))
        conexao.start()


def main_UDP(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print ("Iniciando servidor UDP na porta %s %s\n" % server_address)
    sock.bind(server_address)

    while(True):
        client, address = sock.recvfrom(2048)
        conexao = threading.Thread(target=conexao_cliente_udp,args=(sock, client, address))
        conexao.start()


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)

    # main_TCP(server_address)
    main_UDP(server_address)
