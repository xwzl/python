class Student(object):
    # __slots__ = ('name', 'age')
    class_field = "属于类对象，类似于静态方法"

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.__sex = "female"  # __私有变量 对象._类型__变量名的方式调用

    def get_sex(self):
        return self.__sex

    def set_sex(self):
        self.__sex = "男"

    # __ 开头的是私有方法
    def __private_method(self):
        print("this is a private method")

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


s1 = Student("张三", 13)
s2 = Student("李四", 14)

# 动态属性只属于单对象
s1.names = "清华大学"
s2.name_list = ["清华大学"]
print(s1.names)
s1["name"] = 11
print(s1["name"])

# 这里是给 s1 新增属性，而不是修改
s1.class_field = "修改"
print(s2.class_field)
Student.class_field = "静态变量的修改"

print(s1._Student__sex)
s1._Student__private_method()
