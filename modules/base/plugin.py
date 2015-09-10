class Plugin:

    conn = None

    def __init__(self, conn, cfg):
        self.conn = conn
        self.cfg = cfg

    def parse(self, message):
        raise NotImplementedError
