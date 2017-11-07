from tornado.web import Application,RequestHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line
from json import load
from sqlite3 import connect

define("port",default=8000,help=" file_name --port 8000",type=int)


class Bdayindex(RequestHandler):
    def get(self):
        self.write('Test')


def db_connect(cred_config):
    con=connect(cred_config.get("dbname"))
    return con



if __name__=="__main__":

    app=Application([
        ("/",Bdayindex)
    ])
    options.logging="debug"
    parse_command_line()

    try:
        with open("db_credentials") as f:
            cred_config=load(f)
        db_connect(cred_config)

        server = HTTPServer(app)
        server.listen(options.port)
        IOLoop.instance().start()

    except Exception as e:
        print e






