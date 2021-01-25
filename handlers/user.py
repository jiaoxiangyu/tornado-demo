import time
from abc import ABC

from libs import MyRequestHandler
from logs.log import Logger
from models.models import User


# 查询所有
class GetAllHandler(MyRequestHandler):
    async def get(self):
        users = User.get_all()
        # self.render('user/user.html', users=users)
        return self.resp(data=users)


# 删除
class DeleteByIdHandler(MyRequestHandler):
    async def get(self):
        # 获取请求参数id
        _id = int(self.get_query_argument("id"))
        count = User.delete(_id)
        return self.resp(data=count)


# 添加
class AddHandler(MyRequestHandler):
    async def post(self):
        log = Logger()
        try:
            log.info(self.request.body)
            name = self.get_argument("name")
            pwd = self.get_argument("pwd")
            age = self.get_argument("age")
            sex = self.get_argument("sex")
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            user = User(name, pwd, age, sex, date, date)
            count = user.save()
            return self.resp(data=count)

        except Exception as e:
            log.error("user AddHandler error, {}".format(e))


