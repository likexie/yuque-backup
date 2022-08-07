# -*- coding: utf-8 -*-
#!/usr/bin/python
# @Date : 2022-03-05
# @Author : zhu
# @File : conf.py
# @Software: VS

from pathlib import Path

base_path = Path(__file__).parent

########S 这里不要动########
# 接口api
DOC_FORMAT_DICT = {
    ".html":"body_html",
    ".lake":"body_lake",
    ".draft":"body_draft"
}
API_BASE_URL = "https://www.yuque.com/api/v2"
########S 这里不要动########

########S 一下需要修改部分########
# 个人路径
PERSONAL_PATH = 'xxx'
# 登录token在语雀页面生成
TOKEN = "wRNQMdDijFIh8sD8dJH76UOiXW0Uq93hIHd87DmDrV"
# 备份保存路径
BACKUP_PATH = base_path 

# 保存文档的格式.md .html .lake
# 格式会有问题，可以查看一下文档
# https://www.yuque.com/yuque/developer/docdetailserializer
# https://www.yuque.com/yuque/developer/yr938f
# 要下载什么格式
DOC_FORMAT = ".html"
########S 一下需要修改部分########