# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from requests import Session


class SessionRequest(object):

    def __init__(self, base_url='', **options):
        """
        :param base_url: 用于和参数path进行拼接
        :param kwargs: requests.request 方法支持的所有参数
        method, url=>(base_url + path),
        params=None, data=None, headers=None, cookies=None, files=None,
        auth=None, timeout=None, allow_redirects=True, proxies=None,
        hooks=None, stream=None, verify=None, cert=None, json=None
        """
        self.base_url = base_url
        self.options = options
        self.session = Session()

    def before_request(self, options):
        """请求前 参数处理器"""
        options['url'] = self.base_url + options.pop('path')

        return options

    def after_request(self, response):
        """请求后 响应处理器"""
        return response

    def request(self, **options):
        """请求处理器"""
        # fix python2.7 do'not use {**kwargs}
        options.update(self.options)
        options = self.before_request(options)

        response = self.session.request(**options)

        return self.after_request(response)

    def get(self, **options):
        options.setdefault('allow_redirects', True)
        return self.request(method='GET', **options)

    def post(self, **options):
        return self.request(method='POST', **options)

    def delete(self, **options):
        return self.request(method='DELETE', **options)

    def options(self, **options):
        options.setdefault('allow_redirects', True)
        return self.request(method='OPTIONS', **options)

    def head(self, **options):
        options.setdefault('allow_redirects', False)
        return self.request(method='HEAD', **options)

    def put(self, **options):
        return self.request(method='PUT', **options)

    def patch(self, **options):
        return self.request(method='PATCH', **options)
