import socket

class Connection:

    server = ""
    port = None
    socket = None

    def __init__(self, server, port=6667):
        self.server = server
        self.port = port
        self.connect()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))

    def disconnect(self):
        self.socket.close()

    def send(self, message):
        print("Sending\n{0}".format(message))
        message = bytes(message + '\n', 'UTF-8')
        self.socket.send(message)

    def receive(self):
        recv = self.socket.recv(2048)
        message = str(recv, 'UTF-8').strip('\r\n')
        print("received\n{0}".format(message))
        return message

    def ping(self, message):
        pong = message.split(":")[1]
        self.send("PONG :{}".format(pong))
