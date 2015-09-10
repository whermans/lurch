from modules.base.plugin import Plugin

class WtfPlugin(Plugin):

    def __init__(self, conn, cfg):
        super(WtfPlugin, self).__init__(conn, cfg)

    def parse(self, message):
        if message.find("!wtf") != -1:
            self.wtf(message.split("!wtf ")[1])

    def wtf(self, query):
        resp = ("I don't know what {0} means".format(query))
        self.conn.send("PRIVMSG {0} :{1}".format(self.cfg.channel, resp))

    def request(self, url):
        resp = urllib.request.urlopen(url).read()
