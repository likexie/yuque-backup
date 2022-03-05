# 语雀备份

#### 介绍
用来备份语雀文档，保障资料安全.毕竟在人家服务器上，万一哪一天访问不了，就麻烦了，自己有一份备份心里妥妥的。

#### 软件架构
软件架构说明


#### 安装教程
1. 安装python解释器

#### 使用说明

1. 登录语雀平台：https://www.yuque.com/settings/tokens
2. 授权读取的权限即可
![输入图片说明](images/01.yuque1.png)
![输入图片说明](images/01.shouquan.png)
3. 获取生成的token，放在文件conf.py的TOKEN中
![输入图片说明](images/01.yuque.png)
4. 拉取代码
```python
    安装模块    
    pip install requests
```
5. 执行
python main.py
#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

