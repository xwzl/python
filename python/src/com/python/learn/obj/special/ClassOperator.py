class MyClass:  # 自定义一个类
    def __init__(self, name, age):  # 定义该类的初始化函数
        self.name = name  # 将传入的参数值赋值给成员交量
        self.age = age

    def __str__(self):  # 用于将值转化为字符串形式，等同于 str(obj)
        return "name:" + self.name + ";age:" + str(self.age)

    __repr__ = __str__  # 转化为供解释器读取的形式

    def __lt__(self, record):  # 重载 self<record 运算符
        if self.age < record.age:
            return True
        else:
            return False

    def __add__(self, record):  # 重载 + 号运算符
        return MyClass(self.name, self.age + record.age)


myc = MyClass("Anna", 42)  # 实例化一个对象 Anna，并为其初始化
mycl = MyClass("Gary", 23)  # 实例化一个对象 Gary，并为其初始化
print(repr(myc))  # 格式化对象 myc，
print(myc)  # 解释器读取对象 myc，调用 repr
print(str(myc))  # 格式化对象 myc ，输出"name:Anna;age:42"
print(myc < mycl)  # 比较 myc<mycl 的结果，输出 False
print(myc + mycl)  # 进行两个 MyClass 对象的相加运算，输出 "name:Anna;age:65"

# 参考 README.md ,重载运算符
