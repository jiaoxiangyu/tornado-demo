
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
    def resp(self, code=None, msg=None, desc=None, ext_data=None):
        """返回值格式整理，所有/api/的数据接口，都应该采用此函数处理返回值"""
        resp_dict = {}
        resp_dict['RetSucceed'] = True
        resp_dict['Succeed'] = code == 200 or not code
        if code is None:
            resp_dict['Code'] = code = 200
        else:
            resp_dict['Code'] = code
        if msg is None:
            resp_dict['Message'] = {}
        else:
            resp_dict['Message'] = msg
        if desc is None:
            resp_dict['Desc'] = ''
        else:
            resp_dict['Desc'] = desc
        if ext_data is None:
            resp_dict['extData'] = ''
        else:
            resp_dict['extData'] = ext_data
        json_str = json.dumps(resp_dict, ensure_ascii=False, cls=JSONEncoder)
        return self.write(json_str)