import os

# 项目地址
BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    "port": 8888,
}

# 数据库配置
mysql = {
    "host": "10.0.10.52",
    "user": "root",
    "password": "jxy123456",
    "dbName": "test_info",
    "tableNamePrefix": "tab_"
}

# Application配置
settings = {
    # 设置静态资源引用路路径
    "static_path": os.path.join(BASE_DIR, 'static'),
    # 设置模板路径
    "template_path": os.path.join(BASE_DIR, 'templates'),
    # 取消缓存编译的模板，取消缓存静态文件的hash值，提供追踪信息
    "debug": True,
    # 仅自动重启
    # "autoreload":True,
    # 关闭当前项目自动转义
    # "autoescape":None,
}