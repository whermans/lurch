from modules.base.plugin import Plugin
from urllib.request import urlopen, HTTPError
import json

class UrbanPlugin(Plugin):

    def __init__(self, conn, cfg):
        super(UrbanPlugin, self).__init__(conn, cfg)

    def parse(self, message):
        if "!urban" in message:
            self.urban(message.split("!urban ")[1])
        if "!ud" in message:
            self.urban(message.split("!ud ")[1])

    def urban(self, query):
        if len(query.split()) > 1:
            resp = "Sorry, I only understand single words"
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
        query = ''.join(c for c in query if c.isalnum())
        url = "http://api.urbandictionary.com/v0/define?term={0}".format(query)
        try:
            reply = json.loads(self.fetch(url))
            if len(reply) > 0:
                print(json.dumps(reply, indent=4, sort_keys=True))
                answer = reply["list"][0]["definition"]
        except ValueError:
            pass
        except IndexError:
            pass
        return answer

    def fetch(self, url):
        resp = urlopen(url).read()
        return str(resp, 'utf-8')
