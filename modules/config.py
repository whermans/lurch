import configparser

class Config:

    server = channel = nick = real = password = api_key_1 = ""

    def __init__(self, name):
        c = configparser.ConfigParser()
        c.readfp(open(r'config/{0}.cfg'.format(name)))
        self.server = c.get('params', 'server')
        self.channel = c.get('params', 'channel')
        self.nick = c.get('params','nick')
        self.real = c.get('params','real')
        self.password = c.get('params','password')
        self.api_key_1 = c.get('params', 'api_key_1')


