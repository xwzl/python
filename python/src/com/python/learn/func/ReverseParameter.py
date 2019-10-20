# Python逆向参数收集详解
#
# 所谓逆向参数收集，指的是在程序己有列表、元组、字典等对象的前提下，把它们的元素“拆开”后传给函数的参数。逆向参数收集需要在传入的
# 列表、元组参数之前添加一个星号，在字典参数之前添加两个星号。
def hello_world(name, message):
    print(name, message)


lists = ["Java", "你好"]

# 逆向参数，把元组列表字典等对象进行拆分
hello_world(*lists)

dicts = dict(name="how are", message="python")
hello_world(**dicts)


# 实际上，即使是可变参数，如果程序需要将一个元组传给该参数，那么同样需要使用逆向收集
def foo(name, *nums):
    print("name参数: ", name)
    print("nums参数: ", nums)


my_tuple = (1, 2, 3)
# 使用逆向收集，将my_tuple元组的元素传给nums参数
# *my_tuple 把元组分解为多个参数，*nums 可变参数在把多个参数聚集为元组
foo('hello', *my_tuple)

# 证明 *my_tuple 被分解为多个参数
foo(*my_tuple)
# 不使用逆向收集，my_tuple元组整体传给name参数
foo(my_tuple)

print("字典的逆向收集与列表集合的逆向收集不一样，需要指定两个 **")


def school(name, time, count):
    print("%s 有 %d 年的历史，曾经有 %d 个优秀学子获得诺贝尔奖金" % (name, time, count))


def schools(maps):
    print("%(name)s 有 %(time)d 年的历史，曾经有 %(count)d 个优秀学子获得诺贝尔奖金" % maps)


goods = {
    "name": "清华大学",
    "time": 120,
    "count": 599
}

school(**goods)
schools(goods)