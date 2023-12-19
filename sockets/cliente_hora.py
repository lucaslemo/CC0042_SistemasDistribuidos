import socket
import threading


def receber_mensagens_tcp(sock):
    data = sock.recv(2048)
    print('Agora são: ' + data.decode())
    sock.sendall('0'.encode('utf-8'))
    sock.close()


def receber_mensagens_udp(sock):
    message, address = sock.recvfrom(2048)
    print('Agora são: ' + message.decode())


def main_TCP(server_address):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Conectando %s porta %s" % server_address)

    sock.connect(server_address)
    recepcao = threading.Thread(target=receber_mensagens_tcp, args=(sock,))
    recepcao.start()

    sock.sendall('Qual a hora?'.encode('utf-8'))

    recepcao.join()


def main_UDP(server_address):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ("Enviando requisição para %s porta %s" % server_address)

    recepcao = threading.Thread(target=receber_mensagens_udp, args=(sock,))
    recepcao.start()

    sock.sendto('Qual a hora?'.encode('utf-8'), server_address)

    recepcao.join()


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)

    # main_TCP(server_address)
    main_UDP(server_address)