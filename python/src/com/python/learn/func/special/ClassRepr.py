# Python __repr__()方法：显示属性
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 创建一个Item对象，将之赋给im变量
im = Item('鼠标', 29.8)
# 打印im所引用的Item对象
print(im)

# 当读者运行上面程序时，可能会看到不同的输出结果，at 后的 16 位十六进制数字可能发生改变。但这个输出结果是怎么来的呢？按道理来
# 说，print() 函数只能在控制台打印字符串，而 Item 实例是内存中的一个对象，怎么能直接转换为字符串输出呢？
#
# 事实上，当使用该方法输出 Item 对象时，实际上输出的是 Item 对象的 __repr__() 方法的返回值。

# im 与 im.repr 方法相等
print(im.__repr__())


# __repr__() 是 Python 类中的一个特殊方法，由于 object 类己提供了该方法，而所有的 Python 类都是 object 类的子类，因此所有的 Python 对象都具有 __repr__() 方法。
# 相当于 Java 中的 toString 方法

# 因此，当程序需要将任何对象与字符串进行连接时，都可先调用 __repr__() 方法将对象转换成字符串，然后将两个字符串连接在一起。例如如下代码：
#
#   im str = im.__repr() + ""
#
# __repr__() 是一个非常特殊的方法，它是一个“自我描述”的方法，该方法通常用于实现这样一个功能：当程序员直接打印该对象时，系统将会输出该对象的“自我描述”信息，用来告诉外界
# 该对象具有的状态信息。
#
# object 类提供的 __repr__() 方法总是返回该对象实现类的“类名+object at+内存地址”值，这个返回值并不能真正实现“自我描述”的功能，因此，如果用户需要自定义类能实现“自我描
# 述”的功能，就必须重写 __repr__() 方法。例如下面程序：
class Apple:

    # 实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    # 重写__repr__方法，用于实现Apple对象的“自我描述”
    def __repr__(self):
        return "Apple[color=" + self.color + \
               ", weight=" + str(self.weight) + "]"


a = Apple("红色", 5.68)
# 打印Apple对象
print(a)


class Student:

    def __init__(self, name, class_name, age):
        self.name = name
        self.class_name = class_name
        self.age = age

    def __repr__(self) -> str:
        return "Student[name=" + self.name + ",class_name=" + self.class_name + ",age=" + self.age + "]"


l = Student("小明", "高一一班", "20")
print(l)
