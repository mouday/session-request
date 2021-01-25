# session request

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

```
