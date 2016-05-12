import tornado.ioloop
import tornado.web
import tornado.httpserver

class helloworld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world\n")

class testpage(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="abc">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))

class CustomApplication(tornado.web.Application):
    def __init__(self):
        handles = [
            (r"/", MainHandler),
            (r"/hello", helloworld),
            (r"/test", testpage),
            (r"/story/([0-9]+)", StoryHandler),
        ]
        super(CustomApplication,self).__init__(handles)
# if __name__ == '__main__':
http_server = tornado.httpserver.HTTPServer(CustomApplication)
http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()



