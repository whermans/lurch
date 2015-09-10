#!/usr/bin/env python3
from modules.bot import Bot
from modules.base.connection import Connection
from modules.config import Config

def main():
    cfg = Config("lurch")
    c = Connection(cfg.server)
    b = Bot(c, cfg.nick, cfg.channel, cfg.real, cfg.password)
    try:
        b.run()
    except KeyboardInterrupt:
        c.disconnect()

if __name__ == "__main__":
    main()
