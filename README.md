# session request

![PyPI](https://img.shields.io/pypi/v/session-request.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/session-request)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/session-request)
![PyPI - License](https://img.shields.io/pypi/l/session-request)


以类的形式封装请求接口，支持requests所有参数

Github: [https://github.com/mouday/session-request](https://github.com/mouday/session-request)

pypi: [https://pypi.org/project/session-request](https://pypi.org/project/session-request)


安装
```bash
pip install session-request
```

使用
```python
# -*- coding: utf-8 -*-

from session_request import Request


class ClientApi(Request):
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

```
