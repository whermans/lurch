class Plugin:

    conn = None
    timed = False

    def __init__(self, conn, cfg, timed=False):
        self.conn = conn
        self.cfg = cfg
        self.timed = timed

    def parse(self, message):
        raise NotImplementedError

    def tick(self):
        raise NotImplementedError

    def message(self, resp):
        self.conn.send("PRIVMSG {0} :{1}".format(self.cfg.channel, resp))

