import requests

class RequestsTools(object):
    def __init__(self):
        pass

    def get(self, url, params=None, headers=None):
        # 这个函数的作用是，获取一个已经存在的资源
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        return requests.get(url, params=params, headers=headers)
    
    def post(self, url, data=None, headers=None):
        # 这个函数的作用是，创建一个新的资源
        if data is None:
            data = {}
        if headers is None:
            headers = {}
        return requests.post(url, data=data, headers=headers)
    
    def put(self, url, data=None, headers=None):
        # 这个函数的作用是，更新一个已经存在的资源
        if data is None:
            data = {}
        if headers is None:
            headers = {}
        return requests.put(url, data=data, headers=headers)
    
    def delete(self, url, headers=None):
        # 这个函数的作用是，删除一个已经存在的资源
        if headers is None:
            headers = {}
        return requests.delete(url, headers=headers)
    
    def head(self, url, headers=None):
        # 这个函数的作用是，获取一个资源的元数据
        if headers is None:
            headers = {}
        return requests.head(url, headers=headers)