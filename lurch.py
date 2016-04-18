#!/usr/bin/env python3
from modules.bot import Bot
from modules.base.connection import Connection
from modules.config import Config
from modules.plugins.wtf import WtfPlugin
from modules.plugins.remind import RemindPlugin
from modules.plugins.magic8 import Magic8Plugin
from modules.plugins.urban import UrbanPlugin

def main():
    cfg_name = "lurch"
    cfg = Config(cfg_name)
    c = Connection(cfg.server)
    wtf = WtfPlugin(c, cfg)
    remind = RemindPlugin(c, cfg)
    m = Magic8Plugin(c, cfg)
    u = UrbanPlugin(c, cfg)
    b = Bot(c, cfg.nick, cfg.channel, cfg.real, cfg.password)
    b.install(wtf)
    b.install(remind)
    b.install(m)
    b.install(u)

    try:
        b.run()
    except KeyboardInterrupt:
        c.disconnect()

if __name__ == "__main__":
    main()
