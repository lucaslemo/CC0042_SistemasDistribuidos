from xmlrpc.client import ServerProxy


def main(server_address):
    server = ServerProxy('http://%s:%s' % server_address)
    print(server.get_list())

    time = server.store_list('Primeira mensagem')
    time = server.store_list('Segunda mensagem')
    time = server.store_list('Terceira mensagem')

    print(server.get_list())

    print(server.get_ip())

    time = server.get_current_time()
    count = server.get_count()
    print('Agora são: ' + time)
    print('Foram feitas %d chamadas ao servidor' % count)


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)
    main(server_address)
