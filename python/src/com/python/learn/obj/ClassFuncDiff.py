# Python类实例方法
#
# 通常情况下，在类中定义的方法默认都是实例方法。前面章节中，我们已经定义了不只一个实例方法。不仅如此，类的构造方法理论上也属于实例方法，只不过它比较特殊。
class Person:

    # 类构造方法，也属于实例方法
    def __init__(self, name='Charlie', age=8):
        self.name = name
        self.age = age

    # 下面定义了一个say实例方法
    def say(self, content):
        print(content, self.age)


print("一般来说，实例方法都包含 self 参数")


# Python类方法
#
# Python 类方法和实例方法相似，它最少也要包含一个参数，只不过，类方法中通常将其命名为 cls，且 Python 会自动将类本身绑定给 cls 参数（而不是类对象）。因此，在
# 调用类方法时，无需显式为 cls 参数传参。
#
# 和 self 一样，cls 参数的命名也不是规定的（可以随意命名），只是 Python 程序员约定俗称的习惯而已。
class Bird:
    # class method 修饰的方法是类方法
    @classmethod
    def fly(cls):
        print('类方法fly: ', cls)

    @classmethod
    def ketty(cls):
        print("hello")

    # staticmethod修饰的方法是静态方法
    @staticmethod
    def info(p):
        print('静态方法info: ', p)


# 注意，如果没有 class method，则 Python 解释器会将 fly() 方法认定为实例方法，而不是类方法。
# 类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）
# 调用类方法，Bird类会自动绑定到第一个参数
Bird.fly()
b = Bird()
# 使用对象调用fly()类方法，其实依然还是使用类调用，
# 因此第一个参数依然被自动绑定到Bird类
b.fly()

# 可以看到，不管程序是使用类还是对象调用类方法，Python 都会将类方法的第一个参数绑定到类本身

# Python类静态方法
#
# 静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。
#
# 静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定，也正是因为如此，此方法中无法调用任何类和对象的属性和方法，静态方法其实和类的关系不大。
#
# 静态方法需要使用＠staticmethod修饰
# 类名直接调用静态方法
Bird.info("类名")
# 类对象调用静态方法
b = Bird()
b.info("类对象")


# 在使用 Python 编程时，一般不需要使用类方法或静态方法，程序完全可以使用函数来代替类方法或静态方法。但是在特殊的场景（比如使用工厂模式）下，类方法或静态方法也是不错的选择。

# 定义全局空间的foo函数
def foo():
    print("全局空间的foo方法")


# 全局空间的bar变量
bar = 20


class Bird:
    # 定义Bird空间的foo函数
    @staticmethod
    def foo():
        print("Bird空间的foo方法")

    # 定义Bird空间的bar变量
    bar = 200


# 调用全局空间的函数和变量
foo()
print(bar)
# 调用Bird空间的函数和变量
Bird.foo()
print(Bird.bar)


# 现在问题来了，如果使用类调用实例方法，那么该方法的第一个参数（self）怎么自动绑定呢？
class User:
    def walk(self):
        print(self, '正在慢慢地走')


# 通过类调用实例方法
# 这说明在使用类调用实例方法时，Python 不会自动为第一个参数绑定调用者。实际上也没法自动绑定，因此实例方法的调用者是类本身，而不是对象。
# User.walk()


# 如果程序依然希望使用类来调用实例方法，则必须手动为方法的第一个参数传入参数值。
u = User()
# 显式为方法的第一个参数绑定参数值
User.walk(u)

# 实际上，当通过 User 类调用 walk() 实例方法时，Python 只要求手动为第一个参数绑定参数值，并不要求必须绑定 User 对象，因此也可使用如下代码进行调用：
# 显式为方法的第一个参数绑定fkit字符串参数值
User.walk("SS")

# 总结
#
# Python 的类可以调用实例方法，但使用类调用实例方法时，Python 不会自动为方法的第一个参数 self 绑定参数值；程序必须显式地为第一个参数 self 传参，这种方式调用的方法被称为“未绑定方法”。
# 用类的实例对象访问的类成员方法称为绑定方法；用类名调用的类成员方法称为非绑定方法。
