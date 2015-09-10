from modules.base.plugin import Plugin
import time

class RemindPlugin(Plugin):

    reminders = []

    def __init__(self, conn, cfg):
        super(RemindPlugin, self).__init__(conn, cfg, True)

    def parse(self, message):
        if "!remindme" in message:
            query = message.split("!remindme")
            if len(query) > 1:
                self.remind(query[1])
            else:
                self.help()

    def help(self):
        resp = "Format: !remindme <duration in seconds> <message>"
        self.message(resp)

    def remind(self, query):
        parts = query.split()
        if len(parts) >  1:
            r = Reminder(self.now(), parts[0], ' '.join(parts[1:]))
            self.reminders.append(r)
            resp = "Added reminder!"
        else:
            resp = "Format: !remindme <duration in seconds> <message>"
        self.message(resp)

    def now(self):
        return time.time()

    def tick(self):
        now = self.now()
        for r in self.reminders:
            if r.end < now:
                resp = "Reminder: {0}".format(r.message)
                self.message(resp)
                self.reminders.remove(r)

class Reminder:

    start = duration = end = 0
    message = ""

    def __init__(self, start, duration, message):
        self.duration = duration
        self.message = message
        self.start = start
        self.end = self.add(self.start, self.duration)
        print("Added reminder: {0} {1} {2}".format(message, start, self.end))

    def add(self, start, duration):
        duration = self.toSeconds(duration)
        return start + float(duration)

    def toSeconds(self, duration):
        if self.isNum(duration):
            return duration
        else:
            return 0

    def isNum(self, test):
        try:
            float(test)
            return True
        except ValueError:
            return False

