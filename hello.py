from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

class HelloHandler(RequestHandler):
    def get(self):
        user = self.get_argument('user')
        self.write("Hello, %s" % user)

if __name__ == "__main__":
    handler_mapping = [(r'/?', HelloHandler)]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
