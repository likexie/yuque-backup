import json
import requests

class YQRequest():

    def __init__(self,token):
        self.headers = {
            'X-Auth-Token':token,
            "Content-Type":"application/json"
        }
        self.request = requests

    def get(self, url, headers=dict(), params=None):
        '''
        语雀GET请求接口
        :param param1(int):
        :param param2(int):
        return:
        '''
        if headers:
            self.headers.update(headers)
        resp = self.request.get(url,headers=self.headers,params=params)
        return resp

    def post(self,url,data,headers=dict()):
        self.headers.update(headers)
        data = json.dumps(data)
        resp = self.request.post(url,headers=self.headers,data=data)
        return resp

    def delete(self,url):
        resp = self.request.delete(url,headers=self.headers)
        return resp

    


