from time import time


class School(object):
    # __slots__ = ("address", "name", "rank")

    class_field = "类成员变量"

    def __init__(self, address, name, rank) -> None:
        super().__init__()
        self.address = address
        self.name = name
        self.rank = rank
        self.__score = "503"  # 私有类

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    # 私有方法
    def __check_status(self):
        print("打印分数", self.__score)

    # 获取分数
    def get_score(self):
        return self.__score

    @staticmethod
    def static_method():
        print("工具方法，与成员和类无关")

    @classmethod
    def class_filed_print(cls):
        print("类相关的属性", cls.class_field)


school = School("北京市", "清华大学", "No.1")

# print(school._School__score)

print(school.get_score())

