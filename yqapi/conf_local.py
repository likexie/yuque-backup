# -*- coding: utf-8 -*-
#!/usr/bin/python
# @Date : 2022-03-05
# @Author : zhu
# @File : conf.py
# @Software: VS

from pathlib import Path

base_path = Path(__file__).parent


# 接口api
API_BASE_URL = "https://www.yuque.com/api/v2"
# 登录token在语雀页面生成
TOKEN = "wRNQMdDijFq6UOiXW0Uq93hIRS4mDrGrQB9RBKoV"
# 备份保存路径
BACKUP_PATH = base_path 

# 保存文档的格式.md .html .lake
DOC_FORMAT = ".md"