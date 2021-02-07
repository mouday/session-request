# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from session_request import SessionRequest


class ClientApi(SessionRequest):
    def after_request(self, response):
        """请求后 响应处理器"""
        return response.json()

    def get_request(self):
        options = {
            'path': '/get'
        }
        return self.get(**options)


if __name__ == '__main__':
    base_url = 'http://httpbin.org'
    api = ClientApi(base_url=base_url)
    res = api.get_request()
    print(res['url'])
    # http://httpbin.org/get
