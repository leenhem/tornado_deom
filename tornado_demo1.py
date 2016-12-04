import os.path
import tornado.web
import tornado.httpserver
import tornado.ioloop


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/index.html", MainHandler),
            (r"/static/sytle.css", cssHandler),
        ]
        settings = {
            "template_path":os.path.join(os.path.dirname(__file__),'static'),
            # "template_path": "./static/",
            "static_path":"./static/",
            "debug":True
        }
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        
class cssHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("sytle.css")

def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(88)

    tornado.ioloop.IOLoop.instance().start()

#f __name__ == "__main__":
print (os.path.join(os.path.dirname(__file__),'static'))
main()