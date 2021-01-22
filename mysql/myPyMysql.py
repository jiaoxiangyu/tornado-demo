import pymysql
import config


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
    dbName = config.mysql["dbName"]

    def connet(self):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as err:
            print("查询sql=", sql)
            print("查询失败,", err)
        return res

    def get_all(self, sql):

        res = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as err:
            print("查询sql=", sql)
            print("查询失败,", err)
        return res

    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        if (len(args) > 0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldsSql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s' and table_schema = '%s'" % (
                tableName, self.dbName)
            fields = self.get_all(fieldsSql)
            for item in fields:
                fieldsList.append(item[0])

        # 执行查询数据sql
        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        return resList

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as err:
            print("查询sql=", sql)
            print("事物提交失败, ", err)
            self.db.rollback()
        return count
