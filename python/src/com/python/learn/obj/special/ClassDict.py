# Python __dict__属性：查看对象内部所有属性名和属性值组成的字典
#
# _dict__ 属性用于查看对象内部存储的所有属性名和属性值组成的字典，通常程序直接使用该属性即可。
#
# 程序使用 __dict__ 属性既可查看对象的所有内部状态，也可通过字典语法来访问或修改指定属性的值。


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 28.9)
print(im.__dict__)  # ①
# 通过__dict__访问name属性
print(im.__dict__['name'])
# 通过__dict__访问price属性
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name)  # 键盘
print(im.price)  # 32.8


# 在动态检查对象是否包含某些属性（包括方法〉相关的函数有如下几个：
# hasattr(obj, name)：检查 obj 对象是否包含名为 name 的属性或方法。
# getattr(object, name[, default])：获取 object 对象中名为 name 的属性的属性值。
# setattr(obj, name, value，/)：将obj 对象的 name 属性设为 value。
# 下面程序示范了通过以上函数来动态操作 Python 对象的属性：
class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times

    def info(self):
        print("一条简单的评论，内容是%s" % self.detail)


c = Comment('疯狂Python讲义很不错', 20)
# 判断是否包含指定的属性或方法
print(hasattr(c, 'detail'))  # True
print(hasattr(c, 'view_times'))  # True
print(hasattr(c, 'info'))  # True
# 获取指定属性的属性值
print(getattr(c, 'detail'))  # '疯狂Python讲义很不错'
print(getattr(c, 'view_times'))  # 20
# 由于info是方法，故下面代码会提示：name 'info' is not defined
# print(getattr(c, info, '默认值'))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
# 输出重新设置后的属性值
print(c.detail)
print(c.view_times)

# 从上面最后两行输出来看，程序使用 setattr() 函数可改变 Python 对象的属性值；如果使用该函数对 Python 对象设置的属性不
# 存在，那么就表现为添加属性反正 Python 是动态语言。看如下代码：
# 设置不存在的属性，即为对象添加属性
setattr(c, 'test', '新增的测试属性')
print(c.test)  # 新增的测试属性


# 实际上 setattr() 函数还可对方法进行设置，在使用 setattr() 函数重新设置对象的方法时， 新设置的方法是未绑定方法。
def bar():
    print('一个简单的bar方法')


# 将c的info方法设为bar函数
setattr(c, 'info', bar)
c.info()

# 将c的info设置为字符串'fkit'
setattr(c, 'info', 'fkit')
# 不仅如此，程序完全可通过 setattr() 函数将 info() 方法设置成普通值，这样将会把 info 变成一个属性，而不是方法
print(c.info)

# Python issubclass和isinstance函数：检查类型
#
# Python 提供了如下两个函数来检查类型：
#
#   issubclass(cls, class_or_tuple)：检查 cls 是否为后一个类或元组包含的多个类中任意类的子类。
#   isinstance(obj, class_or_tuple)：检查 obj 是否为后一个类或元组包含的多个类中任意类的对象。
#
# 通过使用上面两个函数，程序可以方便地先执行检查，然后才调用方法，这样可以保证程序不会出现意外情况。
#
# 如下程序示范了通过这两个函数来检查类型：
# 定义一个字符串
hello = "Hello"
# "Hello"是str类的实例，输出True
print('"Hello"是否是str类的实例: ', isinstance(hello, str))
# "Hello"是object类的子类的实例，输出True
print('"Hello"是否是object类的实例: ', isinstance(hello, object))
# str是object类的子类，输出True
print('str是否是object类的子类: ', issubclass(str, object))
# "Hello"不是tuple类及其子类的实例，输出False
print('"Hello"是否是tuple类的实例: ', isinstance(hello, tuple))
# str不是tuple类的子类，输出False
print('str是否是tuple类的子类: ', issubclass(str, tuple))
# 定义一个列表
my_list = [2, 4]
# [2, 4]是list类的实例，输出True
print('[2, 4]是否是list类的实例: ', isinstance(my_list, list))
# [2, 4]是object类的子类的实例，输出True
print('[2, 4]是否是object类及其子类的实例: ', isinstance(my_list, object))
# list是object类的子类，输出True
print('list是否是object类的子类: ', issubclass(list, object))
# [2, 4]不是tuple类及其子类的实例，输出False
print('[2, 4]是否是tuple类及其子类的实例: ', isinstance([2, 4], tuple))
# list不是tuple类的子类，输出False
print('list是否是tuple类的子类: ', issubclass(list, tuple))

# issubclass() 和 isinstance() 两个函数的第二个参数都可使用元组
data = (20, 'fkit')
print('data是否为列表或元组: ', isinstance(data, (list, tuple)))  # True
# str不是list或者tuple的子类，输出False
print('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))
# str是list或tuple或object的子类，输出True
print('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))


# 此外，Python 为所有类都提供了一个 __bases__ 属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。
class A:
    pass


class B:
    pass


class C(A, B):
    pass


print('类A的所有父类:', A.__bases__)
print('类B的所有父类:', B.__bases__)
print('类C的所有父类:', C.__bases__)

# Python 还为所有类都提供了一个 __subclasses__() 方法，通过该方法可以查看该类的所有直接子类，该方法返回该类的所有子类组成的列表。
print('类A的所有子类:', A.__subclasses__())
print('类B的所有子类:', B.__subclasses__())


# Python __call__方法
#
# 前面章节中，我们用 hasattr() 函数判断指定属性（或方法）是否存在，但到底是属性还是方法，则需要进一步判断它是否可调用。程序可通过判断
# 该属性（或方法）是否包含 __call__ 属性来确定它是否可调用
class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def validLogin(self):
        print('验证%s的登录' % self.name)


# 从上面程序的输出结果不难看到，对于 name、 passwd 两个属性，由于它们都是不可调用的，因此程序在判断它们是否包含 __call__ 方法时输出 False；
# 对于 validLogin 方法，由于它是可调用的，因此程序在判断它是否包含 __call__  方法时输出 True。
u = User('crazyit', 'leegang')
# 判断u.name是否包含__call__方法，即判断是否可调用
print(hasattr(u.name, '__call__'))  # False
# 判断u.passwd是否包含__call__方法，即判断是否可调用
print(hasattr(u.passwd, '__call__'))  # False
# 判断u.validLogin是否包含__call__方法，即判断是否可调用
print(hasattr(u.validLogin, '__call__'))  # True


# 实际上，一个函数（甚至对象）之所以能执行，关键就在于 __call__() 方法。实际上 x(arg1, arg2,...) 只是 x.__call__(arg1, arg2, ...) 的快捷
# 写法，因此我们甚至可以为自定义类添加 __call__ 方法，从而使得该类的实例也变成可调用的。
# 定义Role类
class Role:
    def __init__(self, name):
        self.name = name

    # 定义__call__方法
    def __call__(self):
        print('执行Role对象')


r = Role('管理员')
# 直接调用Role对象，就是调用该对象的__call__方法
r()


# 对于程序中的函数，同样既可使用函数的语法来调用它，也可把函数当成对象，调用它的 __call__ 方法。
def foo():
    print('--foo函数--')


# 下面示范了2种方式调用foo()函数
foo()
foo.__call__()
