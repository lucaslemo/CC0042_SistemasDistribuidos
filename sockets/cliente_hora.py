import socket
import threading


def main_TCP(server_address):

    # Inicializa o socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Conectando %s porta %s" % server_address)

    # Faz a coneção com o servidor
    sock.connect(server_address)

    # Envia requisição para o servidor
    sock.sendall('Qual a hora?'.encode('utf-8'))

    # Recebe a resposta do servidor
    data = sock.recv(2048)
    print('Agora são: ' + data.decode())

    # Envia requisição para fechar a conexão e fecha o socket
    sock.sendall('0'.encode('utf-8'))
    sock.close()


def main_UDP(server_address):

    # Inicializa o socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ("Enviando requisição para %s porta %s" % server_address)

    # Envia requisição para o servidor
    sock.sendto('Qual a hora?'.encode('utf-8'), server_address)

    # Recebe a resposta do servidor
    message, address = sock.recvfrom(2048)
    print('Agora são: ' + message.decode())

    # Fecha o socekt
    sock.close()


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)

    main_TCP(server_address)
    # main_UDP(server_address)