# 导入MethodType
from types import MethodType


class Person:
    username = None
    age = None

    def __init__(self, username, age) -> None:
        self.username = username
        self.age = age

    def say(content):
        print(content)

    def __str__(self) -> str:
        return super().__str__()


me = Person("张三", 20)

me.username = "hello"

print(me.age)
print(me.username)

# 动态添加变量
me.skills = "hello world"
print(me.skills)

# 动态删除变量
del me.skills
# 不能访问
# print(me.skills)

# 动态添加方法
me.hello = lambda self: print("动态添加方法", self)
me.hello("1212")

you = Person("test", 12)


def intro_func(self, content):
    print("我是一个人，信息为：%s" % content)


# 使用MethodType对intro_func进行包装，将该函数的第一个参数绑定为p
me.intro = MethodType(intro_func, me)

# 第一个参数已经绑定了，无需传入
# 如果希望动态增加的方法也能自动绑定到第一个参数，则可借助于 types 模块下的 MethodType 进行包装。
me.intro("生活在别处")

me.ketty = intro_func

me.ketty(me, "hello")
