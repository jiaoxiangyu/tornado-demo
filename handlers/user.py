from libs import MyRequestHandler
from models.models import User


# 查询所有
class GetAllHandler(MyRequestHandler):
    async def get(self):
        users = User.get_all()
        self.render('user/user.html', users=users)


# 删除
class DeleteByIdHandler(MyRequestHandler):
    async def get(self):
        # 获取请求参数id
        _id = int(self.get_query_argument("id"))
        count = User.delete(_id)
        return self.resp(ext_data=count)
