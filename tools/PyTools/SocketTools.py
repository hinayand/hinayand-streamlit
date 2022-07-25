import socket


class SocketUDPTools(object):
    def __init__(self):
        self.temp_message = None
        self.data = None
        self.self_ip = None
        self.target_address = None
        self.udp_socket_io = None
        self.ip = None
        self.socket_io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_ip(self):
        try:
            self.socket_io.connect(('8.8.8.8', 80))
            self.ip = self.socket_io.getsockname()[0]
        finally:
            self.socket_io.close()
        return self.ip

    def send_udp_message(self, host, port, data):
        self.udp_socket_io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.target_address = (host, port)
        self.udp_socket_io.bind(self.target_address)
        self.udp_socket_io.send(data)
        self.udp_socket_io.close()
        del self.target_address

    def get_message(self, port):
        self.self_ip = self.get_ip()
        self.udp_socket_io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket_io.bind((self.self_ip, port))
        message, address = self.udp_socket_io.recvfrom(1024)
        self.data = (address, message)
        return self.data
