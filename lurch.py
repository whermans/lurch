#!/usr/bin/env python3
from modules.bot import Bot
from modules.base.connection import Connection
from modules.config import Config
from modules.plugins.wtf import WtfPlugin
from modules.plugins.remind import RemindPlugin

def main():
    cfg_name = "lurch"
    cfg = Config(cfg_name)
    c = Connection(cfg.server)
    wtf = WtfPlugin(c, cfg)
    remind = RemindPlugin(c, cfg)
    b = Bot(c, cfg.nick, cfg.channel, cfg.real, cfg.password)
    b.install(wtf)
    b.install(remind)
    try:
        b.run()
    except KeyboardInterrupt:
        c.disconnect()

if __name__ == "__main__":
    main()
