from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


class RPC:
    def __init__(self, ip):
        self.ip = ip
        self.count = 0
        self.list = []

    def get_current_time(self):
        self.count += 1
        time = datetime.now()
        timeString = time.strftime('%Y-%m-%d %H:%M')
        return timeString

    def store_list(self, string):
        self.count += 1
        self.list.append(string)
        return 'String inserida com sucesso'
    
    def get_list(self):
        self.count += 1
        if len(self.list) == 0:
            return 'A lista esta vazia'
        return self.list

    def get_ip(self):
        self.count += 1
        return self.ip

    def get_count(self):
        self.count += 1
        return self.count


def main(server_address):
    server = SimpleXMLRPCServer(server_address)
    rpc = RPC(server_address[1])
    server.register_instance(rpc)

    print ("Iniciando servidor RPC na porta %s %s\n" % server_address)
    server.serve_forever()


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)
    main(server_address)
