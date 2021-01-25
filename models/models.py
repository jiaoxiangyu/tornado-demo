import time
from mysql.orm import ORM


class User(ORM):
    def __init__(self, name, pwd, age, sex, create_time, update_time):
        self.name = name
        self.pwd = pwd
        self.age = age
        self.sex = sex
        self.status = 0
        self.create_time = create_time
        self.update_time = update_time



