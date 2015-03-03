#!/usr/bin/env python

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from ctron import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5050)
IOLoop.instance().start()
