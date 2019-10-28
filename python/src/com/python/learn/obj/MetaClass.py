# type() 函数更适合于动态地创建相对简单的类，如果要创建更复杂的类，则需要通过 MetaClass（元类）的方式。
#
# MetaClass（元类），简单的理解，就是创建类的类，即创建类之后，再由类来创建实例进行应用。使用元类可以在创建类时动态修改类定义。为了使用元类动态修改类定义，程序需要先定义元类。
# 注意，不要从字面上去理解元类的含义，事实上，MetaClass 中的 Meta 这个词根，起源于希腊语词汇 meta，包含“超越”和“改变”的意思。
#
# 定义元类时，需令其继承与 type 类，且默认的命名习惯是，让类名以 MetaClass 结尾。不仅如此，元类中需要定义并实现 __new__() 方法（一定要有返回值）。因为元类在创建类时，该 __new__() 方
# 法将会被调用，用来生成新建的类。
#
# 之所有要求元类继承 type 并实现 __new__() 方法，是因为在创建类时，内部调用了 type 的 __new__() 方法为这个类分配内存空间，当内存分配完成后，便会调用 type 的 _init__ 方法初始化。

# 定义Item元类，继承type
class ItemMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)


# 上面程序定义了一个 ItemMetaClass，该类继承了 type 类，并重写了 __new__ 方法，在重写该方法时为目标类动态添加了一个 cal_price 方法。
# 元类的 __new__ 方法的作用是：当程序使用 class 定义新类时，如果指定了元类，那么元类的 __new__ 方法就会被自动执行。
# 定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 定义cellPhone类
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 上面程序定义了 Book 和 CellPhone 两个类，在定义这两个类时都指定了元类信息，因此当 Python 解释器在创建这两个类时，ItemMetaClass 的 __new__ 方法就会被调用，用于修改这两个类。
#
# ItemMetaClass 类的 __new__ 方法会为目标类动态添加 cal_price 方法，因此，虽然在定义 Book、CellPhone 类时没有定义 cal_price() 方法，但这两个类依然有 cal_price() 方法。如下
# 程序测试了 Book、CellPhone 两个类的 cal_price() 方法：
b = Book("Python基础教程", 89)
b.discount = 0.76
# 创建Book对象的cal_price()方法
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
# 创建CellPhone对象的cal_price()方法
print(cp.cal_price())
