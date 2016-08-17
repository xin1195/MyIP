#!/usr/bin/env python3
# _*_coding:utf-8_*_

import os

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="bZJc2sWbQLKodScdGkHn/VKTNam0R0kRvJ5/xJ89E=",
    xsrf_cookies=True,
    debug=False,

)
