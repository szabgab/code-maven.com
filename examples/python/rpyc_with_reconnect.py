import rpyc
class ReConn(object):
    def __init__(self, server):
        self.server = server
        self.connect()

    def connect(self):
        print("connecting")
        self.conn = rpyc.classic.connect(self.server)

    def execute(self, code):
        try:
            self.conn.execute(code)
        except EOFError:
            self.connect()
            self.conn.execute(code)

    def eval(self, code):
        try:
            return self.conn.eval(code)
        except EOFError:
            self.connect()
            return self.conn.eval(code)

