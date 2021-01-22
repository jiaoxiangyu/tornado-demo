
from mysql.orm import ORM


class User(ORM):
    def __init__(self, id, name, pwd, age, status, create_time, update_time):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.age = age
        self.status = status
        self.create_time = create_time
        self.update_time = update_time


