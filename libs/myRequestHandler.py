
import json
import tornado.web
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    '用于格式化mongo取出数据中的ObjectId对象'
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class MyRequestHandler(tornado.web.RequestHandler):
    def resp(self, code=None, msg=None, data=None):
        """返回值格式整理，所有/api/的数据接口，都应该采用此函数处理返回值"""
        resp_dict = {}
        if code is None:
            resp_dict['code'] = 200
        else:
            resp_dict['code'] = code
        if msg is None:
            resp_dict['msg'] = '成功'
        else:
            resp_dict['msg'] = msg
        if data is not None:
            resp_dict['data'] = data
        json_str = json.dumps(resp_dict, ensure_ascii=False, cls=JSONEncoder)
        return self.write(json_str)