import platform
import tornado.ioloop
import tornado.httpserver


from application import Application
import config

if __name__ == "__main__":
    # 建立路由表
    server = tornado.httpserver.HTTPServer(Application())
    # 监听端口
    server.bind(config.options['port'])
    # 启动进程
    if platform.system().lower() == 'windows':
        server.start()   # Fork 单个进程
    else:
        # server.start(0)  # Fork 多个子进程
        server.start()  # Fork 单个进程
    print('Tornado app running')
    # 开始事件
    tornado.ioloop.IOLoop.current().start()