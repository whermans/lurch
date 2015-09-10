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
        if len(query.split()) > 1:
            resp = "I'm sorry, I only understand single words"
        else:
            resp = ("I don't know what {0} means".format(query))
            try:
                answer = self.lookup(query)
                if answer != "":
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
        try:
            reply = json.loads(self.fetch(url))
            if len(reply) > 0 and 'text' in reply[0]:
                answer = reply[0]['text']
        except ValueError:
            pass
        return answer

    def fetch(self, url):
        resp = urlopen(url).read()
        return str(resp, 'utf-8')
