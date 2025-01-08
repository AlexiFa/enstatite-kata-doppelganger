class Authorizer:
    def __init__(self, status):
        self.status = status

    def authorize(self):
        return self.status