from modules.base.connection import Connection
from time import sleep
import threading

class Bot:

    nick = channel = real = password =""
    conn= None
    plugins = []
    timed = []

    def __init__(self, connection, nick, channel, real, password):
        self.conn = connection
        self.nick = nick
        self.channel = channel
        self.real = real
        self.password = password
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
            if "422" in recv:
                break
        self.conn.send("JOIN #{0}".format(self.channel))

    def install(self, plugin):
        self.plugins.append(plugin)
        if plugin.timed:
            self.timed.append(plugin)

    def run(self):
        threading.Timer(0.5, self.run).start()
        for t in self.timed:
            t.tick()
        recv = self.conn.receive()
        if recv != "":
            self.parse(recv)

    def parse(self, recv):
        if "PING" in recv:
            self.conn.ping(recv)
        for p in self.plugins:
            p.parse(recv)
