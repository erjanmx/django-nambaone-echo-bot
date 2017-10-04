#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from threading import Timer

os.environ["DJANGO_SETTINGS_MODULE"] = "bot_project.settings"

import cherrypy
import django

django.setup()
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler


class DjangoApplication(object):

    def run(self, host, port):
        cherrypy.config.update({
            'server.socket_host': host,
            'server.socket_port': port,
            'engine.autoreload_on': False,
            'log.screen': True
        })

        cherrypy.log("Loading and serving Django application at http://{}:{}".format(host, port))
        cherrypy.tree.graft(WSGIHandler())
        cherrypy.engine.start()
        cherrypy.engine.block()


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8001

    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])

    DjangoApplication().run(host, port)
