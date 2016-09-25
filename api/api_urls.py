#!/usr/bin/env python3
# _*_coding:utf-8_*_
from api.controller.getIpHandler import ApiGetIpHandler

api_urls = [

    (r"/", ApiGetIpHandler),                                            # 获取请求客户端的外网ip
    (r"/api/get_ip", ApiGetIpHandler),                                            # 获取请求客户端的外网ip
]
