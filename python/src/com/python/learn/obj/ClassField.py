# 我们知道，无论是在类中定义的属性还是方法，在类的外部，都无法直接调用它们，因此，我们完全可以把类看做是一个独立的作用域（称为类命名空间），则类属性其实就是定义
# 在类命名空间内的变量（类方法其实就是定义的类命名空间中的函数）。
#
# 根据定义属性的位置不同，类属性又可细分为类属性（后续用类变量表示）和实例属性（后续用实例变量表示）。
#
# 类变量（类属性）
#
# 类变量指的是定义在类中，但在各个类方法外的变量。类变量的特点是：所有类的实例化对象都可以共享类变量的值，即类变量可以在所有实例化对象中作为公用资源。
#
# 注意，类变量推荐直接用类名访问，但也可以使用对象名访问。
class Address:
    # 类对象，相当于 Java 的静态属性
    detail = '广州'
    # 对象
    post_code = '510660'

    def __init__(self):
        self.depict = None

    @staticmethod
    def info():
        # 尝试直接访问类变量
        # print(detail) # 报错
        # 通过类来访问类变量
        print(Address.detail)  # 输出 广州
        print(Address.post_code)  # 输出 510660


# 创建 2 个类对象
addr1 = Address()
addr1.info()
addr2 = Address()
addr2.info()
# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr1.info()
addr2.info()


# 当然，Python 也支持使用对象来访问该对象所属类的类属性（此方式不推荐使用）
class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2016-06-16'

    def info(self):
        print('info方法中: ', self.item)
        print('info方法中: ', self.date)


rc = Record()
print(rc.item)  # '鼠标'
print(rc.date)  # '2016-06-16'
rc.info()

# 在 Python 中，除了可以通过类名访问类属性之外，还可以动态地为类和对象添加类变量。
Address.depict = "佛山很美"
print(Address.depict)
print(Address.depict)


# 实例变量（实例属性）
#
# 实例变量指的是定义在类的方法中的属性，它的特点是：只作用于调用方法的对象。
#
# 注意，实例变量只能通过对象名访问，无法通过类名直接访问。
#
# Python 允许通过对象访问类变量，但无法通过对象修改类变量的值。因为，通过对象修改类变量的值，不是在给“类变量赋值”，而是定义新的实例变量。

class Inventory:
    # 定义两个类变量
    item = '鼠标'
    quantity = 2000

    # 定义实例方法
    def change(self, item, quantity):
        # 下面赋值语句不是对类变量赋值，而是定义新的实例变量
        self.item = item
        self.quantity = quantity


# 类中，实例变量和类变量可以同名，但是在这种情况下，使用类对象将无法调用类变量，因为它会首选实例变量，因此这也是不推荐“类变量使用对象名调用”的原因。
# 创建Inventory对象
iv = Inventory()
iv.change('显示器', 500)
# 访问iv的item和quantity实例变量
print(iv.item)  # 显示器
print(iv.quantity)  # 500
# 访问Inventory的item和quantity类变量
print(Inventory.item)  # 鼠标
print(Inventory.quantity)  # 2000

# 即便程序通过类修改了两个类变量的值，程序中 Inventory 的实例变量的值也不会受到任何影响
Inventory.item = '类变量item'
Inventory.quantity = '类变量quantity'
# 访问iv的item和quantity实例变量
print(iv.item)
print(iv.quantity)

iv2 = Inventory()
iv2.change('键盘', 300)
iv.item = 'iv实例变量item'
iv.quantity = 'iv实例变量quantity'
print(Inventory.item)
print(Inventory.quantity)

print(iv.item)
print(iv.quantity)

iv.color = "red"
print(iv.color)
# 因为 color 实例变量仅 iv 对象有，iv2 对象并没有，因此下面这行代码会报错
# print(iv2.color)
