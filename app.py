import tornado.web
from tornado import web, httpserver, ioloop
from view import LoginHander, RegisterHandler, IndexHandler
from postgres import Postgres

# 路由
app = web.Application([
    (r"/login", LoginHander),
    (r"/register", RegisterHandler),
    (r"/index", IndexHandler)
])

# 设置
setting = {
    'template_path': 'tempalte',
    'Debug': True,

}

class run(object):
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8080)
    print('http://127.0.0.1:8080/login')
    tornado.ioloop.IOLoop.current().start()

# socket服务端
if __name__ == '__main__':
    Postgres()
    run()
