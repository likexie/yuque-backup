# -*- coding: utf-8 -*-
#!/usr/bin/python
# @Date : 2022-03-05
# @Author : zhu
# @File : main.py
# @Software: VS
import traceback
from yqapi import *
from pprint import pprint
from pathlib import Path
import os
from yqapi.conf import PERSONAL_PATH,DOC_FORMAT_DICT

base_path = BACKUP_PATH / 'backup'
if not base_path.is_dir():
    os.makedirs(base_path)

# 获取用户基本信息
# resp = YQUsers().get_user_info()

# 获取仓库列表
repo_list = YQRepo(PERSONAL_PATH).get_list().get('data')
if not repo_list:
    print('请检查conf.py中的token是否正确')
    exit()
print('总库数量:',len(repo_list))
for repo in repo_list:
    print("仓库名称：",repo.get('name'))
    print("文章数量：",repo.get('items_count'))
    namespace = repo.get('namespace')
    # 创建仓库文件夹
    repo_path = base_path / repo.get('name')
    if not repo_path.is_dir():
        os.makedirs(repo_path)
    # 获取仓库文档列表
    doc_list = YQDocs(namespace).get_list().get('data')
    for doc in doc_list:
        print('开始下载……',doc.get('title'))
        slug = doc.get('slug')
        file_name = doc.get('title') + DOC_FORMAT
        save_path = os.path.join(str(repo_path),file_name.replace("/", "-"))
        file_data = YQDocs(namespace).get_info_by_id(slug)
        body = DOC_FORMAT_DICT.get(DOC_FORMAT,'body')
        try:
            with open(save_path,'wb')as f:
                is_content = file_data.get('data').get(body)
                if is_content:
                    content = """<link type="text/css" href="../css/lake-content-v1.css" rel="stylesheet"/>"""+is_content
                    f.write(content.encode('utf8'))
                else:
                    print(file_name,":",'没有格式：' , DOC_FORMAT)
                    for format,body in DOC_FORMAT_DICT.items():
                        print('下载其他格式：%s' % format)
                        is_content = file_data.get('data').get(body)
                        if is_content:
                            content = """<link type="text/css" href="../css/lake-content-v1.css" rel="stylesheet"/>"""+is_content
                            f.write(content.encode('utf8'))
                            print(file_name,":没有%s格式的"%DOC_FORMAT,'->格式更换为：%s' % format)
        except Exception as e:
            print("文件",file_name,'保存失败',str(traceback.format_exc()))

print('完成下载……')
