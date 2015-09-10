from modules.base.plugin import Plugin
from urllib.request import urlopen, HTTPError
import json

class WtfPlugin(Plugin):

    def __init__(self, conn, cfg):
        super(WtfPlugin, self).__init__(conn, cfg)

    def parse(self, message):
        if "!wtf" in message:
            self.wtf(message.split("!wtf ")[1])

    def wtf(self, query):
        resp = ("I don't know what {0} means".format(query))
        try:
            answer = self.lookup(query)
            resp = "{0}: {1}".format(query, answer)
        except ValueError:
            pass
        except HTTPError:
            pass
        self.message(resp)

    def lookup(self, query):
        answer = ""
        query= ''.join(c for c in query if c.isalnum())
        url = "http://api.wordnik.com:80/v4/word.json/{0}/definitions?limit=1&includeRelated=true&sourceDictionaries=all&useCanonical=true&includeTags=false&api_key={1}".format(query, self.cfg.api_key_1)
        print("Looking up {0}".format(url))
        try:
            reply = json.load(self.request(url))
            answer = reply.text
        except ValueError:
            pass
        return answer

    def request(self, url):
        resp = urlopen(url)
