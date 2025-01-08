class Notifier:
    def __init__(self):
        self.notifs = []

    def notify(self, user, message):
        self.notifs.append((user, message))