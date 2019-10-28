from typing import Any


# 类似于 Java 的抽象类
# 从上面的运行结果来看，通过使用元类可以动态修改程序中的一批类，对它们集中进行某种修改。这个功能在开发一些基础性框架时非常有用，程序可以通过使用元类
# 为某一批需要具有通用功能的类添加方法。
class MetaClassQq(type):

    # class 指定 meta Class 初始化的时候，都会调用这个方法
    # 用于新增一些通用方法
    def __new__(cls, name, bases, attrs) -> Any:
        # 动态新增 number 方法
        attrs['number'] = lambda self: print("%s 账号的长度是 %d:" % (self.service, self.number_size))
        return super().__new__(cls, name, bases, attrs)


class QqGame(metaclass=MetaClassQq):

    def __init__(self, service, number_size):
        self.service = service
        self.number_size = number_size

    def setService(self, service):
        self.service = service
        print("设置 name 方法")

    def getService(self):
        return self.service

    services = property(getService, setService)


class QqFlyCars(metaclass=MetaClassQq):
    def __init__(self, service, number_size):
        self.service = service
        self.number_size = number_size

    def setService(self, service):
        self.service = service
        print("QqFlyCars 设置 name 方法")

    def getService(self):
        return self.service

    services = property(getService, setService)


game = QqGame("QQ 游戏", 12)
fly = QqFlyCars("QQ 飞车", 12)

fly.number()
game.number()

game.services = "飞机"
game.number()


class DogLi:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def setName(self, name):
        self.name, self.height = name

    def getName(self):
        return self.name, self.height

    names = property(getName, setName)


li = DogLi("12", 12)
print(li.name, li.height)

li.names = "ll"
print(li.names)
