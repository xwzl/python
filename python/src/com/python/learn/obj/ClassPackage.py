# python 封装
#
# 封装（Encapsulation）是面向对象的三大特征之一（另外两个是继承和多态），它指的是将对象的状态信息隐藏在对象内部，不允许外部程序直接访问对象内部信息，而是通过该类所提供的方法来实现对
# 内部信息的操作和访问。
#
# 就好比使用计算机，我们只需要使用计算机提供的键盘，就可以达到操作计算机的目的，至于在敲击键盘时计算机内部是如何工作，我们根本不需要知道。
#
# 封装机制保证了类内部数据结构的完整性，因为使用类的用户无法直接看到类中的数据结构，只能使用类允许公开的数据，很好地避免了外部对内部数据的影响，提高了程序的可维护性。总的来说，对一个类
# 或对象实现良好的封装，可以达到以下目的：
#
#   隐藏类的实现细节。
#   让使用者只能通过事先预定的方法来访问数据，从而可以在该方法里加入控制逻辑，限制对属性的不合理访问。
#   可进行数据检查，从而有利于保证对象信息的完整性。
#   便于修改，提高代码的可维护性。
#
# 为了实现良好的封装，需要从以下两个方面来考虑：
#
#   将对象的属性和实现细节隐藏起来，不允许外部直接访问。
#   把方法暴露出来，让方法来控制对这些属性进行安全的访问和操作。
#
# 因此，实际上封装有两个方面的含义：把该隐藏的隐藏起来，把该暴露的暴露出来。
#
# Python 并没有提供类似于其他语言的 private 等修饰符，因此 Python 并不能真正支持隐藏。为了隐藏类中的成员，Python 玩了一个小技巧：只要将 Python 类的成员命名为以双下画线开头的，Python 就
# 会把它们隐藏起来。
class User:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __hide(self):
        print('示范隐藏的hide方法', self.age)

    def getName(self):
        return self.__name

    def setName(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3～8之间')
        self.__name = name

    name = property(getName, setName)

    def setAge(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户名年龄必须在18在70之间')
        self.__age = age

    def getAge(self):
        return self.__age

    age = property(getAge, setAge)


# 上面程序将 User 的两个实例变量分别命名为 __name 和 __age，这两个实例变量就会被隐藏起来，这样程序就无法直接访问 __name、__age 变量，只能通过 setName()、
# getName()、setAge()、getAge() 这些访问器方法进行访问，而 setName()、setAge() 会对用户设置的 name、age 进行控制，只有符合条件的 name、age 才允许设置。
# 创建User对象
u = User("文曲星", 80)
# 对name属性赋值，实际上调用setName()方法
u.name = 'fk1'  # 引发 ValueError: 用户名长度必须在3～8之间
print(u.age)

u.name = 'fkit'
u.age = 25
print(u.name)  # fkit
print(u.age)  # 25

# 上面程序还定义了一个 __hide() 方法，这个方法默认是隐藏的
# 尝试调用隐藏的__hide()方法
# u.__hide()

# 最后需要说明的是，Python 其实没有真正的隐藏机制，双下画线只是 Python 的一个小技巧，Python 会“偷偷”地改变以双下画线开头的方法名，会在这些方法名前添加单下画线
# 和类名。因此上面的 __hide() 方法其实可以按如下方式调用（通常并不推荐这么干）：
# 调用隐藏的__hide()方法
u._User__hide()

# 类似的是，程序也可通过为隐藏的实例变量添加下画线和类名的方式来访问或修改对象的实例变量。
# 对隐藏的__name属性赋值
u._User__name = 'fk'
# 访问User对象的name属性（实际上访问__name实例变量）
print(u.name)

# 总结
#
# Python 并没有提供真正的隐藏机制，所以 Python 类定义的所有成员默认都是公开的；如果程序希望将 Python 类中的某些成员隐藏起来，那么只要让该成员的名字以双下画线开头即可。
#
# 即使通过这种机制实现了隐藏，其实也依然可以绕过去。
