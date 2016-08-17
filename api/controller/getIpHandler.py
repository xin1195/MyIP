#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Administrator 
# Time 2016/8/17.
import tornado.web
from tornado import gen


class ApiGetIpHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @gen.coroutine
    def get(self):
        self.write(self.request.remote_ip)
