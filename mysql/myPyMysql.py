import time

import pymysql
import config
from logs.log import Logger


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class PyMySQL(object):
    host = config.mysql["host"]
    user = config.mysql["user"]
    password = config.mysql["password"]
    db_name = config.mysql["dbName"]

    def connet(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db_name)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        log = Logger()
        res = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as err:
            log.error("查询sql: {}".format(sql))
            log.error("查询失败: {}".format(err))
        return res

    def get_all(self, sql, *args):
        log = Logger()
        res = ()
        try:
            self.connet()
            self.cursor.execute(sql, args)
            res = self.cursor.fetchall()
            self.close()
        except Exception as err:
            log.error("查询sql: {}, args: {}".format(sql, args))
            log.error("查询失败: {}".format(err))
        return res

    def get_all_obj(self, sql, table_name, *args):
        # 封装返回参数
        resList = []
        fieldsList = []
        if (len(args) > 0):  # 自定义返回值
            for item in args:
                fieldsList.append(item)
        else:  # 查询全部返回值
            fields_sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = %s and table_schema = %s"
            fields = self.get_all(fields_sql, table_name, self.db_name)
            for item in fields:
                fieldsList.append(item[0])

        # 执行查询数据sql
        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                if type(x) == 'datetime':
                    x = time.strftime("%Y-%m-%d %H:%M:%S", x)
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        return resList

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql, *args):
        return self.__edit(sql, args)

    def delete(self, sql, *args):
        return self.__edit(sql, args)

    def __edit(self, sql, *args):
        log = Logger()
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql, args)
            self.db.commit()
            self.close()
        except Exception as err:
            log.error("更新sql: {}, args: {}".format(sql, args))
            log.error("更新失败: {}".format(err))
            self.db.rollback()
        return count
