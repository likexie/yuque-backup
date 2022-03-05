# -*- coding: utf-8 -*-
#!/usr/bin/python
# @Date : 2022-03-05
# @Author : zhu
# @File : yuque.py 
# @Software: VS
# @desc：获取语雀基本信息

from yqapi.interface import *
from yqapi.utils import YQRequest
from yqapi.conf import API_BASE_URL,TOKEN

# 用户信息
class YQUsers(Users):
    
    def __init__(self, name=None):
        if name:
            self.url = API_BASE_URL+'/users/%s' % name
        else:
            self.url = API_BASE_URL+'/user'
        
    def get_user_info(self,name=None):
        data = YQRequest(TOKEN).get(self.url).json()
        return data


# 知识库信息
class YQRepo(Common):

    def __init__(self, login):
        self.url = API_BASE_URL + '/users/%s/repos' %(login)

    def get_list(self, offset=None, limit=None):
        params = dict()
        params['offset'] = offset
        params['limit'] = limit
        resp = YQRequest(TOKEN).get(url=self.url, params=params)
        return resp.json()

    def get_info_by_id(self,id):
        pass


# 文档类
class YQDocs(Common):

    def __init__(self, namespace):
        self.url = API_BASE_URL+'/repos/%s/docs' % namespace

    def get_list(self, offset=None, limit=None ):
        params = dict()
        params['offset'] = offset
        params['limit'] = limit
        resp = YQRequest(TOKEN).get(url=self.url, params=params)
        return resp.json()

    def get_info_by_id(self, slug, raw=None):
        self.url += '/%s' % slug
        params = {'raw':raw}
        resp = YQRequest(TOKEN).get(url=self.url, params=params)
        return resp.json()
