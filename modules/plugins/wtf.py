from modules.base.plugin import Plugin
from urllib.request import urlopen

class WtfPlugin(Plugin):

    def __init__(self, conn, cfg):
        super(WtfPlugin, self).__init__(conn, cfg)

    def parse(self, message):
        if "!wtf" in message:
            self.wtf(message.split("!wtf ")[1])

    def wtf(self, query):
        resp = ("I don't know what {0} means".format(query))
        answer = self.lookup(query)
        if answer != "":
            resp = answer
        self.message(resp)

    def lookup(self, query):
        answer = url = ""
        try:
            reply = self.request(url)
        except ValueError:
            pass
        return answer

    def request(self, url):
        resp = urlopen(url).read()
