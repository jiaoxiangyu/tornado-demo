import tornado.web
from handlers import main
from handlers import user
import config
import os


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # 主页
            (r"/", main.MainHandler),

            # 用户列表
            (r"/user", user.GetAllHandler),

            # 删除用户
            (r"/user/delete", user.DeleteByIdHandler),

            # 添加用户
            (r"/user/add", user.AddHandler),

            # StaticFileHandler,要放在所有路由的最下面
            (r'/(.*)$', tornado.web.StaticFileHandler, {"path": os.path.join(config.BASE_DIR, "static/html"),
                                                        "default_filename": "index.html"}),

        ]

        super(Application, self).__init__(handlers, **config.settings)