from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime


class RPC:
    def __init__(self):
        self.count = 0

    def get_current_time(self):
        self.count += 1
        time = datetime.now()
        timeString = time.strftime('%H:%M:%S')
        return timeString

    def get_count(self):
        return self.count


def main(server_address):
    server = SimpleXMLRPCServer(server_address)
    rpc = RPC()
    server.register_instance(rpc_server)

    print ("Iniciando servidor RPC na porta %s %s\n" % server_address)
    server.serve_forever()


if __name__ == '__main__':
    # Ip e porta do servidor
    server_address = ('localhost', 20001)
    main(server_address)
