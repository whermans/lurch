#!/usr/bin/env python3
from modules.bot import Bot
from modules.base.connection import Connection
from modules.config import Config
from modules.plugins.wtf import WtfPlugin

def main():
    cfg_name = "lurch"
    cfg = Config(cfg_name)
    c = Connection(cfg.server)
    p = WtfPlugin(c, cfg)
    plugins = []
    plugins.append(p)
    b = Bot(c, cfg.nick, cfg.channel, cfg.real, cfg.password, plugins)
    try:
        b.run()
    except KeyboardInterrupt:
        c.disconnect()

if __name__ == "__main__":
    main()
