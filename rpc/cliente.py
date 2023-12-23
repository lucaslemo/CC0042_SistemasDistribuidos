from xmlrpc.client import ServerProxy


def main(server_address):
    server = ServerProxy('http://%s:%s', % server_address)
    time = server.get_current_time()
    count = server.get_count()
    print('Agora são: ' + time)
    print('Foram feitas ' + count + 'chamadas ao servidor')


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)
    main(server_address)
