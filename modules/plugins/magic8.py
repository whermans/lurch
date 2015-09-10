from modules.base.plugin import Plugin
import random

class Magic8Plugin(Plugin):

    replies = [
            'It is certain',
            'It is decidely so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy, try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Don\'t count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
            ]

    def __init__(self, conn, cfg):
        super(Magic8Plugin, self).__init__(conn, cfg, True)

    def parse(self, message):
        if "!magic8" in message:
            if "?" in message:
                self.message(random.choice(self.replies))
            else:
                self.message("That does not appear to be a question")

    def tick(self):
        pass
