# Python 的子类也会继承得到父类的构造方法，但如果子类有多个直接父类，那么会优先选择排在最前面的父类的构造方法。
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是:', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('我是一个顾客，我的爱好是: %s,地址是%s' % (self.favorite, self.address))


# Manager继承了Employee、Customer
class Manager(Employee, Customer):
    pass


m = Manager(25000)
m.work()
# m.info()

# 为了让 Manager 能同时初始化两个父类中的实例变量，Manager 应该定义自己的构造方法，即重写父类的构造方法。Python 要求，如果子类重写了父类的构造方法，那么子类的构造方法必须调用父类的构造方法。
#
# 子类的构造方法调用父类的构造方法有两种方式：
#
#   使用未绑定方法，这种方式很容易理解。因为构造方法也是实例方法，当然可以通过这种方式来调用。
#   使用 super() 函数调用父类的构造方法。
#
# 注意，当子类继承多个父类是，super() 函数只能用来调用第一个父类的构造方法，而其它父类的构造方法只能使用未绑定的方式调用。
help(super)


# Manager继承了Employee、Customer
class Manager(Employee, Customer):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('--Manager的构造方法--')
        # 通过super()函数调用父类的构造方法
        super().__init__(salary)
        # 与上一行代码的效果相同
        # super(Manager, self).__init__(salary)
        # 使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, address)


# 创建Manager对象
m = Manager(25000, 'IT产品', '广州')
m.work()
m.info()
