from modules.base.connection import Connection
from time import sleep

class Bot:

    nick = channel = real = password =""
    conn= None
    plugins = None

    def __init__(self, connection, nick, channel, real, password, plugins = []):
        self.conn = connection
        self.nick = nick
        self.channel = channel
        self.real = real
        self.password = password
        self.plugins = plugins
        self.register()

    def register(self):
        sleep(2)
        self.conn.send("USER {0} 0 * {1}".format(self.nick, self.real))
        self.conn.send("PASS {0}".format(self.password))
        self.conn.send("NICK {}".format(self.nick))
        while 1:
            recv = self.conn.receive()
            if "PING" in recv:
                self.conn.ping(recv)
            if "372" in recv:
                break
        self.conn.send("JOIN {0}".format(self.channel))

    def run(self):
        while 1:
            recv = self.conn.receive()
            if recv != "":
                self.parse(recv)

    def parse(self, recv):
        if "PING" in recv:
            self.conn.ping(recv)
        for p in self.plugins:
            p.parse(recv)
