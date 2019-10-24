# 子类扩展了父类，子类是一种特殊的父类。大部分时候，子类总是以父类为基础，额外增加新的方法。但在一些场景中，子类需要重写父类的方法。
#
# 例如，鸟类都包含了飞翔方法，其中驼鸟是一种特殊的鸟类，因此驼鸟应该是鸟的子类，它也将从鸟类获得飞翔方法，但这个飞翔方法明显不适合驼鸟，为此，驼鸟需要重写鸟类的方法。
class Bird:
    # Bird类的fly()方法
    def fly(self):
        print("我在天空里自由自在地飞翔...")


class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("我只能在地上奔跑...")


# 创建Ostrich对象
os = Ostrich()
# 执行Ostrich对象的fly()方法，将输出"我只能在地上奔跑..."
os.fly()


# 使用未绑定方法调用被重写的方法
#
# 如果在子类中调用重写之后的方法，Python 总是会执行子类重写的方法，不会执行父类中被重写的方法。如果需要在子类中调用父类中被重写的实例方法，那该怎么办呢？
#
# 别忘了，Python 类相当于类空间，因此 Python 类中的方法本质上相当于类空间内的函数。所以，即使是实例方法，Python 也允许通过类名调用。区别在于：在通过类名调用实例方法
# 时，Python 不会为实例方法的第一个参数 self 自动绑定参数值，而是需要程序显式绑定第一个参数 self。这种机制被称为未绑定方法。
class BaseClass:

    def bitch(self):
        print("This is a rain day!")


class HappyClass(BaseClass):

    def bitch(self):
        super().bitch()
        print("This a sunny day!")
        # 调用父类方法
        BaseClass.bitch(self)


happy = HappyClass()
happy.bitch()


# 我们知道，Python 中内置有一个 object 类，它是所有内置类型的共同祖先，也是所有没有显式指定父类的类（包括用户自定义的）的共同祖先。因此在实际编程过程中，如果想实现与某个内
# 置类型具有类似行为的类时，最好的方法就是将这个内置类型子类化。
#
# 内置类型子类化，其实就是自定义一个新类，使其继承有类似行为的内置类，通过重定义这个新类实现指定的功能。
#
# 举个例子，如下所示创建了一个名为 newDict 的类，其中 newDictError 是自定义的异常类：
class NewDictError(ValueError):
    """如果向newDict 添加重复值，则引发此异常"""


class NewDict(dict):
    """不接受重复值的字典"""

    def __setitem__(self, key, value):
        if value in self.values():
            print(key in self)
            print(self[key] != value)
            print(key not in self)
            print((key in self and self[key] != value) or (key not in self))
            if ((key in self and self[key] != value) or (key not in self)):
                raise NewDictError("这个值已经存在，并对应不同的键")
        super().__setitem__(key, value)


demoDict = NewDict()
demoDict['key'] = 'value'
demoDict['other_key'] = 'value2'
print(demoDict)
demoDict['other_key2'] = 'valu1e'
print(demoDict)


def test_if(i):
    if i > 2 or i < 10:
        print(i)


test_if(1)


# 比如，list 类型用来管理序列，如果一个类需要在内部处理序列，那么就可以对 list 进行子类化
class MyList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def dir(self, nesting=0):
        offset = " " * nesting
        print("%s%s/" % (offset, self.name))
        for element in self:
            if hasattr(element, 'dir'):
                element.dir(nesting + 1)
            else:
                print("%s %s" % (offset, element))


demoList = MyList('C语言中文网')
demoList.append('http://c.biancheng.net')
print(demoList.dir())
