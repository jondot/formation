class DummyLogger(object):
    def __init__(self):
        self.messages = []

    def bind(self, **kwargs):
        self.context = kwargs
        return self

    def debug(self, msg, **kwargs):
        print("dummy logger: {}".format(msg))
        self.messages.append(["debug", msg, kwargs, self.context])

    def info(self, msg, **kwargs):
        print("dummy logger: {}".format(msg))
        self.messages.append(["info", msg, kwargs, self.context])

    def warn(self, msg, **kwargs):
        print("dummy logger: {}".format(msg))
        self.messages.append(["warn", msg, kwargs, self.context])
