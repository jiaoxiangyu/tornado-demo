from logs.log import Logger
from .myPyMysql import PyMySQL
import config


class ORM(object):
    # 表名前缀
    table_name_prefix = config.mysql["tableNamePrefix"]

    def save(self):
        # insert into tableName (field1, field2) values(value1, value2)
        #                &        &   &             &    &
        # 表名
        table_name = config.mysql["tableNamePrefix"] + self.__class__.__name__.lower()
        fields_str = values_str = "("
        for field in self.__dict__:
            fields_str += (field + ",")
            if isinstance(self.__dict__[field], str):
                values_str += ("'" + self.__dict__[field] + "',")
            else:
                values_str += (str(self.__dict__[field]) + ",")
        # (field1, field2)
        fields_str = fields_str[:len(fields_str) - 1] + ")"
        # (value1, value2)
        values_str = values_str[:len(values_str) - 1] + ")"
        sql = "insert into " + table_name + " " + fields_str + " values " + values_str
        log = Logger()
        log.info(sql)
        db = PyMySQL()
        return db.insert(sql)

    @classmethod
    def delete(cls, _id):
        # delete from tableName where id = ?
        if _id <= 0:
            return 0
        table_name = cls.table_name_prefix +(cls.__name__).lower()
        sql = "delete from {} where id = %s".format(table_name)
        db = PyMySQL()
        return db.delete(sql, _id)

    @classmethod
    def update(cls, sql, *args):
        db = PyMySQL()
        return db.update(sql, args)

    @classmethod
    def get_all(cls):
        # select * from tableName
        table_name = cls.table_name_prefix +(cls.__name__).lower()
        sql = "select * from {}".format(table_name)
        db = PyMySQL()
        return db.get_all_obj(sql, table_name)

    @classmethod
    def filter(cls):
        pass