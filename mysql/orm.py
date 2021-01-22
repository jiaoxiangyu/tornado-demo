from .myPyMysql import PyMySQL
import config


class ORM(object):
    # 表名前缀
    table_name_prefix = config.mysql["tableNamePrefix"]

    def save(self):
        # insert into tableName (name,age) values('tyui',32)
        #                &        &   &             &    &
        # 表名
        table_name = (self.__class__.__name__).lower()
        fieldsStr = valuesStr = "("
        for field in self.__dict__:
            fieldsStr += (field + ",")
            if isinstance(self.__dict__[field], str):
                valuesStr += ("'" + self.__dict__[field] + "',")
            else:
                valuesStr += (str(self.__dict__[field]) + ",")
        # (name,age)
        fieldsStr = fieldsStr[:len(fieldsStr) - 1] + ")"
        # ('tyui',32)
        valuesStr = valuesStr[:len(valuesStr) - 1] + ")"
        sql = "insert into " + table_name + " " + fieldsStr + " values " + valuesStr

        print(sql)
        db = PyMySQL()
        db.insert(sql)

    @classmethod
    def delete(cls, _id):
        # delete from tableName where id = ?
        if _id <= 0:
            return 0
        table_name = cls.table_name_prefix +(cls.__name__).lower()
        sql = "delete from " + table_name + " where id = " + str(_id)
        db = PyMySQL()
        return db.delete(sql)

    @classmethod
    def get_all(cls):
        # select * from tableName
        table_name = cls.table_name_prefix +(cls.__name__).lower()
        sql = "select * from " + table_name
        db = PyMySQL()
        return db.get_all_obj(sql, table_name)

    @classmethod
    def filter(cls):
        pass